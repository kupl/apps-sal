d = dict()
n = int(input())
s = input().rstrip()
sum1 = 0


def f(c):
    return chr(ord(c) - ord('A') + ord('a'))


for i in range(len(s)):
    c = s[i]
    if (i + 1) % 2 == 1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    elif f(c) in d:
        if d[f(c)] > 0:
            d[f(c)] -= 1
        else:
            sum1 += 1
    else:
        sum1 += 1
print(sum1)
