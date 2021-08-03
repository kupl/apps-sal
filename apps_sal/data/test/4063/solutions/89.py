n = int(input())
dn = list(map(int, input().split()))
dn.sort()
a = dn[n // 2 - 1]
b = dn[n // 2]

cnt = 0
for i in range(a, b):
    cnt += 1

print(cnt)
