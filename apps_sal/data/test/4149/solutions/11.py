import sys
limit = 2750132
# limit = 20
mark = [1 for _ in range(limit)]
member = [0 for _ in range(limit)]
m = [0 for _ in range(limit + 1)]
prime = []
ans = []
n = 2
primeSet = set()
mem = {}
num = int(input())
dic = {}
dic2 = {}
a = list(map(int, sys.stdin.readline().split()))
arr1 = []
arr2 = []
for v in a:
    member[v] += 1


def seive(l):
    nonlocal n
    while(n * n <= l):
        if mark[n] == 1:
            next = n * 2
            c = 2
            # prime.append(n)
            primeSet.add(n)
            while(next < l):
                mark[next] = 0
                next += n
                c += 1
        n += 1


seive(limit)
# print(member[:22])
for i in range(2, limit):
    if mark[i] == 1:
        prime.append(i)
        primeSet.add(i)
for i in range(17984):
    # idex = prime[prime[i]-1]
    dic[str(prime[i])] = prime[prime[i] - 1]
    dic[str(prime[prime[i] - 1])] = prime[i]
# print('Primeset',primeSet)
for v in a:
    next = str(v)
    if v not in primeSet:
        # print('No', v)
        for i in range(2, limit):
            if v % i == 0:
                need = v // i
                m[need] += 1;
                dic2[next] = need
                arr2.append(v)
                break
    else:
        m[dic.get(next)] += 1
        arr1.append(v)
# for v in a:
#     if v in primeSet :
#         arr2.append(v)
#     else:
#         arr1.append(v)
arr1 = sorted(arr1, reverse=True)
arr2 = sorted(arr2, reverse=True)
# print(arr1)
# print(arr2)
for v in arr2:
    if member[v]:
        remove = dic2.get(str(v))
        if member[remove]:
            ans.append(v)
            member[remove] -= 1
            member[v] -= 1
for v in arr1:
    if member[v]:
        remove = dic.get(str(v))
        if member[remove]:
            ans.append(min(remove, v))
            member[remove] -= 1
            member[v] -= 1
# print(m)
if len(ans) != num:
    raise Exception('Not enough member')
else:
    print(*ans)
# print(ans)
# print(member[:22])
# print('Dic:',dic)
# print('dic2',dic2)
