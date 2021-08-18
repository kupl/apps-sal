N = int(input())
originalN = 0 + N
if N == 2:
    print(1)
    return
ans = 0
primenum = [2]
count = [0 for _ in range(int(N**0.5) + 2)]
for k in range(3, len(count), 2):
    if count[k] == 0:
        primenum.append(k)
        for j in range(k, len(count), k):
            count[j] = 1


def factorization(n):
    lis = []
    k = 0
    while primenum[k] <= n:
        if n % primenum[k] == 0:
            c = 0
            while n % primenum[k] == 0:
                n //= primenum[k]
                c += 1
            lis.append([primenum[k], c])
        else:
            k += 1
            if k > len(primenum) - 1:
                break
    if n > 1:
        lis.append([n, 1])
    return lis


list1 = factorization(N - 1)
# print(factorization(N-1))
ans1 = 1
for k in range(len(list1)):
    ans1 *= list1[k][1] + 1
ans1 -= 1
ans += ans1

# print(ans1)


def operation(K):
    N = originalN
    while N % K == 0:
        N //= K
    if N % K == 1:
        return True
    else:
        return False


list2 = factorization(N)
# print(list2)
factorlist = [1]

for l in range(len(list2)):
    list3 = []
    for j in range(list2[l][1]):
        for k in range(len(factorlist)):
            list3.append(factorlist[k] * list2[l][0]**(j + 1))
    factorlist += list3

factorlist = factorlist[1:-1]
# print(factorlist)
ans2 = 1
for item in factorlist:
    if operation(item):
        # print(item)
        ans2 += 1


ans += ans2
# print(ans2)

print(ans)
