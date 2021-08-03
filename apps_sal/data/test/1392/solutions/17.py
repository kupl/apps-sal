n, k = map(int, input().split())
t = [input() for i in range(n)]
for i in '0123456789'[: k + 1]:
    t = [j for j in t if i in j]
print(len(t))
