(a, b, k) = map(int, input().split())
n = range(a, b + 1)
for i in sorted(set(n[:k]) | set(n[-k:])):
    print(i)
