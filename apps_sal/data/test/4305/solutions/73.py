H, A = list(map(int, input().split()))
cnt = 0
while H > 0:
    cnt = cnt + 1
    H = H - A

print(cnt)
