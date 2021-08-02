n, m = map(int, input().split())
a = [i for i in range(1, m + 1)]

for _ in range(n):
    l, r = map(int, input().split())
    for x in range(l, r + 1):
        if x in a:
            a.remove(x)

print(len(a))
print(*a)
