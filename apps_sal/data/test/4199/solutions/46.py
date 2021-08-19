(n, k) = map(int, input().split())
s = 0
for m in map(int, input().split()):
    if m >= k:
        s += 1
print(s)
