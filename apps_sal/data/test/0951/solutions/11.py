k = int(input())
n = list(map(int, list(input())))
a = [n.count(i) for i in range(10)]
s = sum(n)
ans = 0
i = 0
while s < k:
    while a[i] > 0 and s < k:
        a[i] -= 1
        a[9] += 1
        s += 9 - i
        ans += 1
    i += 1
print(ans)
