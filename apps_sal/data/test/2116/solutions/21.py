n, m, k = map(int, input().split())
p = list(map(int, input().split()))

r = 0


for i in range(0, n):
    a = list(map(int, input().split()))
    for j in range(0, len(a)):
        index = p.index(a[j])
        r += index + 1
        p.insert(0, p.pop(index))

print(r)
