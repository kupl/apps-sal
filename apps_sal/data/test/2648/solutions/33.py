n = int(input())
a = list(map(int, input().split()))

d = {}
m = 0
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        m += 1
print(m - 1) if (n-m) % 2 else print(m)
