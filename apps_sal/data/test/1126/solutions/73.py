(n, x, m) = map(int, input().split())
an = [0] * m
check = [0] * m
an[0] = x
check[x] = 1
for i in range(1, m + 1):
    x = x ** 2 % m
    if check[x] != 0:
        break
    else:
        check[x] = i + 1
        an[i] = x
num = i - check[x] + 1
ans = sum(an[:check[x] - 1])
kazu = n - len(an[:check[x] - 1])
re = sum(an[check[x] - 1:i])
ans += kazu // num * re
ans += sum(an[check[x] - 1:i - (num - kazu % num)])
print(ans)
