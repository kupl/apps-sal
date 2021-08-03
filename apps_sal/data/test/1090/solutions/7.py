def count(s):
    c = 0

    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            c += 1
    return c


n, k = list(map(int, input().split()))
s = input()
a = [str(c) for c in s]
cmax = n - 1
p = count(a)
while 1:
    if p == cmax:
        break
    elif p == cmax + 1:
        p -= 1
        break
    elif k > 0:
        p += 2
        k -= 1
    else:
        break

print(p)
