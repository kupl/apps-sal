L = str(input())
mod = 10 ** 9 + 7

# a + b = a xor b を満たすのは a, b の bit が一つも被っていないとき
ans = 1
three = [1] * (len(L) + 1)
for i in range(len(L)):
    ans *= 3
    ans %= mod
    three[i + 1] = ans

# print(three)
x = 1
for i in range(len(L)):
    if L[i] == "0":
        y = x * 2
        #print(three[len(L) - i - 1], y, i)
        y *= three[len(L) - i - 1]
        # print(y)
        #y %= mod
        ans -= y
        ans %= mod
    else:
        x *= 2
        x %= mod

print(ans)
