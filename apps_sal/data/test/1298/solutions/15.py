n = int(input())
a = list(map(int, input()))
d = []
for i in range(len(a)):
    d.append(a[i])
    while len(d) >= 2 and d[-1] + d[-2] == 1:
        d.pop()
        d.pop()
        n -= 2
print(n)
