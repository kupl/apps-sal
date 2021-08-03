n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [a[-1]]
for i in range(n - 2, -1, -1):
    if b[0] > b[-1]:
        b = [a[i]] + b
    else:
        b.append(a[i])
print(*b)
