N = int(input())
H = list(map(int, input().split()))

res = H[0]

for i in range(1, N):
    if H[i] >= H[i - 1]:
        res += H[i] - H[i - 1]

print(res)
