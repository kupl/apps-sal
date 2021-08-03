N = int(input())
H = list(map(int, input().split()))

h = [0 for i in range(N - 1)]
ans = 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        h[i] = 1

count = 0
ans = 0
for i in h:
    if i == 1:
        count += 1
        if ans < count:
            ans = count
    else:
        count = 0

print(ans)
