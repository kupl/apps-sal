n, k = map(int, input().split())
snukes = [False] * n
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    A = [n - 1 for n in a]
    for i in range(d):
        snukes[A[i]] = True
print(snukes.count(False))
