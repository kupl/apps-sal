N = int(input())
A = list(map(int, input().split()))
count = [0] * (10 ** 5 + 1)
for a in A:
    count[a] += 1
ans = 0
for i in range(1, 10 ** 5):
    X = count[i - 1] + count[i] + count[i + 1]
    ans = max(ans, X)
print(ans)
