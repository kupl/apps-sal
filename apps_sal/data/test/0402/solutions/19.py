(n, m) = map(int, input().split())
l = 240 - m
ss = []
x = [i * 5 + 5 for i in range(n)]
for i in range(n + 1):
    if sum(x[:i]) <= l:
        ss.append(i)
print(max(ss))
