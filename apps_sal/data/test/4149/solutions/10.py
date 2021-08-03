from collections import Counter
se = set()
odd = dict()
mapi = dict()


def seive(n):
    nonlocal odd
    nonlocal se
    nonlocal mapi
    prime = [True for i in range(n + 1)]
    p = 2
    while(p * p <= n):
        if prime[p]:
            for i in range(2 * p, n + 1, p):
                prime[i] = False
                if i % 2 == 1:
                    if i not in odd:
                        odd[i] = i // p
        p += 1
    new = [0]
    count = 0
    for i in range(2, n + 1):
        if prime[i]:
            new.append(i)
            se.add(i)
            mapi[i] = count
            count += 1
    return new


def largest(k):
    for i in range(k // 2, 1, -1):
        if k % i == 0:
            return i


main = seive(2750131)
n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
d = dict(Counter(l))
w = set(l)
# k=[0]*2*n
ans = []

for i in range(2 * n):
    if l[i] in se and d[l[i]] != 0:
        val = mapi[l[i]] + 1
        # print(val)
        # print(val)
        if val in w and d[val] != 0 and val != 1:
            ans.append(val)
            d[val] -= 1
            d[l[i]] -= 1
    elif d[l[i]] != 0:
        if l[i] % 2 == 0:
            val = l[i] // 2
            if d[val] != 0 and val in w:
                ans.append(l[i])
                d[val] -= 1
                d[l[i]] -= 1
        else:
            val = odd[l[i]]
            if d[val] != 0 and val in w:
                ans.append(l[i])
                d[val] -= 1
                d[l[i]] -= 1
print(*ans)
