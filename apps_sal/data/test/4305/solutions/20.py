(H, A) = map(int, input().split())
cnt = 0
while H > 0:
    H -= A
    cnt += 1
print(cnt)
