N = int(input())
H = list(map(int, input().split()))
result = 1
H_high = H[0]
for i in range(1, N):
    if H[i] >= H_high and H[i] >= H[i - 1]:
        result += 1
        H_high = H[i]
print(result)
