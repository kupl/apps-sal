a, b, k = map(int, input().split())
r = range(2)
an = sorted(set(range(a, min(a + k, b + 1))) | set(range(max(a, b - k + 1), b + 1)))
for i in an:
    print(i)
