from collections import Counter as C
s = input()
c = C(s)
n = len(s)
a = c.get('a', 0)
m = n - a
if m & 1:
    print(":(")
    return
m //= 2
m += a
t = s[:m]
if t + ''.join(c for c in t if c != 'a') != s:
    print(":(")
    return
print(t)
