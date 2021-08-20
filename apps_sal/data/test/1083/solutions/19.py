n = int(input())
sum = (1 + n) * n // 2
print(sum % 2)
a = sum // 2
ans = []
while a:
    if a > n:
        ans += [n]
        a -= n
        n -= 1
    else:
        ans += [a]
        a = 0
print(len(ans), end=' ')
for i in ans:
    print(i, end=' ')
