

n = int(input())

r = ["NO", "YES"]

d = {}

for _ in range(n):
    x, k = list(map(int, input().split(" ")))
    a = d.get(k, -1)
    if a + 1 < x:
        print(r[0])
        return
    elif a + 1 == x:
        d[k] = x

print(r[1])
