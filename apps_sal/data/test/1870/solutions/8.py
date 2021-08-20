(n, c) = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
s = 1
for i in range(n - 1):
    if t[i + 1] - t[i] <= c:
        s += 1
    else:
        s = 1
print(s)
