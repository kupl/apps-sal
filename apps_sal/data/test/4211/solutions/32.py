n = int(input())
b = [int(i) for i in input().split()]
a = [b[0]]
for x in range(n - 2):
    s = min(b[x], b[x + 1])
    a.append(s)
a.append(b[-1])
print(sum(a))
