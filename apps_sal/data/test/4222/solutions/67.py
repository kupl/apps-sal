N, K = list(map(int, input().split()))
ans = [0] * N
count = 0
for i in range(K):
    d = int(input())
    array = list(map(int, input().split()))
    for j in range(d):
        ans[array[j] - 1] += 1
for k in ans:
    if k == 0:
        count += 1
print(count)
