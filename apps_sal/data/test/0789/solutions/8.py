s = input()
ans = 1


def f(k):
    if k == '4':
        return 0
    return 1


for i in range(len(s)):
    ans = (ans << 1) + f(s[i])
print(ans - 1)
