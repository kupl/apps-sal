n = list(map(int, input().split()))
k = int(input())
for _ in range(k):
    n[n.index(max(n))] *= 2
print(sum(n))
