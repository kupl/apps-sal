L = str(input())
mod = 10 ** 9 + 7
ans = 1
three = [1] * (len(L) + 1)
for i in range(len(L)):
    ans *= 3
    ans %= mod
    three[i + 1] = ans
x = 1
for i in range(len(L)):
    if L[i] == '0':
        y = x * 2
        y *= three[len(L) - i - 1]
        ans -= y
        ans %= mod
    else:
        x *= 2
        x %= mod
print(ans)
