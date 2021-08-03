a, b = map(int, input().split())
L = list(map(str, input().split()))
L.pop(0)
for i in range(a - 1):
    c = list(map(str, input().split()))
    c.pop(0)
    L = list(set(L) & set(c))
print(len(L))
