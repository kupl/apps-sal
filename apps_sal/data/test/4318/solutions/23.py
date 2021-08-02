N = int(input())
H = list(map(int, input().split()))

max_h = 0
cnt = 0
for i in range(N):
    if H[i] >= max_h:
        max_h = H[i]
        cnt += 1

print(cnt)
