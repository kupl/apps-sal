N = int(input())
H = list(map(int, input().split()))

lowc = 0

for i in range(1, N):
    if H[i - 1] > H[i]:
        lowc += H[i - 1] - H[i]

print(lowc + H[-1])
