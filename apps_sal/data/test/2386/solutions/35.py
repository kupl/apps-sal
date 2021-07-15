n = int(input())
aa = list(map(int, input().split()))

for i in range(n):
    aa[i] -= i

aa.sort()

mid = aa[n // 2]

print(sum(abs(a - mid) for a in aa))
