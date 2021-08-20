n = int(input())
p = list(map(int, input().split()))
memo = 0
for i in range(n - 2):
    if p[i] > p[i + 1] and p[i + 1] > p[i + 2] or (p[i] < p[i + 1] and p[i + 1] < p[i + 2]):
        memo += 1
print(memo)
