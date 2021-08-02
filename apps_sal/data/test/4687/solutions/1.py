N, K = map(int, input().split())
arr = [0] * (10**5 + 1)

for i in range(N):
    a, b = map(int, input().split())
    arr[a] += b

s = 0
for i in range(10**5 + 1):
    s += arr[i]
    if s >= K:
        print(i)
        break
