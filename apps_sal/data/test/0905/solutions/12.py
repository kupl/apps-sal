[n, s] = [int(x) for x in input().split()]
t = [-1]
for i in range(1, n + 1):
    [a, b] = [int(x) for x in input().split()]
    if a + b * 0.01 <= s:
        if b == 0:
            t.append(0)
        else:
            t.append(100 - b)
t.sort(reverse=True)
print(t[0])
