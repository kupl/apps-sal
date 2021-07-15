import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

n, k = read_ints()
s = input().strip()
ss = set(s)
minss = min(ss)
maxss = max(ss)
t = ''

if k > n:
    t = s + minss * (k - n)
else:
    t = list(s[:k])
    for i in reversed(list(range(k))):
        if t[i] < maxss:
            for x in sorted(ss):
                if x > t[i]:
                    t[i] = x
                    break
            cut = i
            break
    for i in range(cut + 1, k):
        t[i] = minss
    t = ''.join(t)

print(t)

