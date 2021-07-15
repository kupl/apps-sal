n = int(input())
h = [0] + list(map(int, input().split()))
cnt = 0
for i in range(n):
    if h[i + 1] > h[i]:
        cnt += h[i+1] - h[i]
print(cnt)
