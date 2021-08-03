N = int(input())
A = list(map(int, input().split()))

count = [0] * (N + 1)

for i in range(N):
    count[A[i]] += 1

# print(count)

total = 0
for j in range(1, N + 1):
    cj = count[j] * (count[j] - 1) // 2
    # print(cj)
    total = total + cj

ans = total
for k in range(N):
    ans = total - (count[A[k]] - 1)
    print(ans)
