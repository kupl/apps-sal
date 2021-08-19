(n, x) = [int(elem) for elem in input().split()]
ms = []
for i in range(n):
    m = int(input())
    ms.append(m)
res = len(ms)
x -= sum(ms)
res += x // min(ms)
print(res)
