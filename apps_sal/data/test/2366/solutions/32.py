import collections
N = int(input())
A = list(map(int, input().split()))

cc = collections.Counter(A)
L = list(cc.values())

total = 0
for i in range(len(L)):
    total += L[i] * (L[i] - 1) // 2

ans = 0
for a in A:
    temp = cc[a] * (cc[a] - 1) // 2
    ttemp = (cc[a] - 1) * (cc[a] - 2) // 2
    ans = total - temp + ttemp
    print(ans)
