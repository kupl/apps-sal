N = int(input())
H = list(map(int, input().split()))
H.insert(0, 0)
res = 0
for i in range(1, N + 1):
    if (H[i] - H[i - 1]) > 0:
        res += (H[i] - H[i - 1])
print(res)
