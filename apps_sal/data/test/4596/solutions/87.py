n = int(input())
a = list(map(int, input().split()))
ma = len(bin(10**9))
for i in range(n):
    cnt = 0
    while a[i] % 2 == 0:
        a[i] /= 2
        cnt += 1
    ma = min(ma, cnt)
print(ma)
