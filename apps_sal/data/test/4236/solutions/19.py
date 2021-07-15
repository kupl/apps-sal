n, m = map(int, input().split())
a = list(range(1, m+1))
for i in range(n):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        if x in a: a.remove(x)
print(len(a))
for x in a:
    print(x, end=" ")

