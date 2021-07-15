n, k = list(map(int, input().split()))
cnt = 0
while k > 0 and n >= 2:
    cnt += (n - 1) * 2 - 1
    n -= 2
    k -= 1
print(cnt)
