(n, k) = map(int, input().split())
cnt = 0
while k % 2 == 0:
    k = k // 2
    cnt += 1
print(cnt + 1)
