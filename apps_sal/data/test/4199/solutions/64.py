n, k = map(int, input().split())
H = list(map(int, input().split()))

cnt = 0

for i in range(n):
    cnt += H[i] >= k

print(cnt)
