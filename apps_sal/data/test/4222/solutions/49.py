n, k = map(int, input().split())
s = set()
for _ in range(k):
    tmp = int(input())
    arr = list(map(int, input().split()))

    for a in arr:
        s.add(a)

print(n - len(s))
