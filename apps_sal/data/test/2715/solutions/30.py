MAX = pow(10, 16) + 1000
K = int(input())
N = 50
kaisu = [K // N for _ in range(N)]
ans = [-1 for _ in range(N)]
nokori = K % N
for i in range(nokori):
    kaisu[i] += 1
# print(kaisu)

for i in range(N):
    temp = (N + 1) * kaisu[i] + N - 1 - K
    ans[i] = temp

print(N)
print(*ans)
