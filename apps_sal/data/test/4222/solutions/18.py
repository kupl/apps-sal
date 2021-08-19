(n, k) = map(int, input().split())
s = [i for i in range(1, n + 1)]
for _ in range(k):
    d = int(input())
    arr = list(map(int, input().split()))
    for a in arr:
        if a in s:
            s.remove(a)
print(len(s))
