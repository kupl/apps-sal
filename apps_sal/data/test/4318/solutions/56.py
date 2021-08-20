N = int(input())
H = list(map(int, input().split()))
maximum = H[0]
cnt = 1
for i in range(1, N):
    if H[i] >= maximum:
        maximum = H[i]
        cnt += 1
print(cnt)
