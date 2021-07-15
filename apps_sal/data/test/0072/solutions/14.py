n = int(input())
a = input()
b = input()
c = input()

def count(s, n):
    cnt = {}
    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
    maxc = 0
    for c in cnt:
        if cnt[c] > maxc: maxc = cnt[c]
    if len(s) == maxc and n == 1:
        return maxc - 1
    else:
        return min(maxc+n, len(s))

ac = count(a, n)
bc = count(b, n)
cc = count(c, n)

if ac > bc and ac > cc:
    print("Kuro")
elif bc > ac and bc > cc:
    print("Shiro")
elif cc > bc and cc > ac:
    print("Katie")
else:
    print("Draw")
