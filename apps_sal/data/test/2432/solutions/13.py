lip = [0, 5, 3, 2, 4, 1]
n = int(input())
a = []
for i in range(6):
    a.append(n % 2)
    n //= 2
a.reverse()
b = [0] * 6
for i in range(6):
    b[lip[i]] = a[i]
ans = 0
k = 1
# print(a)
# print(b)
for i in range(6):
    ans += k * b[-i - 1]
    k *= 2
print(ans)
