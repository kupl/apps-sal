(n, x) = map(int, input().split())
l = []
for i in range(0, n):
    l.append(int(input()))
x -= sum(l)
cnt = x // min(l)
print(n + cnt)
