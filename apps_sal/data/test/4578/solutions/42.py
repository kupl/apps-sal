(n, x) = [int(x) for x in input().split()]
m = []
for i in range(n):
    m.append(int(input()))
x -= sum(m)
res = n
res += x // min(m)
print(res)
