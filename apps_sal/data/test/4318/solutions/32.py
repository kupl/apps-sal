N = int(input())
H = list(map(int, input().split()))

c = 1
h = H[0]

for i in range(1, N):
    if h <= H[i]:
        h = H[i]
        c = c + 1

print(c)
