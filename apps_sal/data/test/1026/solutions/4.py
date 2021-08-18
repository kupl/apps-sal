n = int(input())
b = list(map(int, input().split()))
c = dict()
for i in range(n):
    bi = b[i]
    df = bi - (i + 1)
    c[df] = c.get(df, 0) + i + 1 + df
print(max(c.values()))
