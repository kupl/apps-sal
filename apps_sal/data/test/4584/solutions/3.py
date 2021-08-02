n = int(input())
a = [0, 0] + list(map(int, input().split()))

no_buka = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    no_buka[a[i]] += 1

for j in range(1, n + 1):
    print((no_buka[j]))
