import collections


def palindromic(f, l):
    if l % 2 == 0:
        return len(odds(f)) == 0
    else:
        return len(odds(f)) == 1


def odds(f):
    return [k for (k, v) in list(f.items()) if v % 2 == 1]


def evens(f):
    return [k for (k, v) in list(f.items()) if v % 2 == 0 and v > 0]


s = input()
f = collections.defaultdict(int)
l = len(s)
for c in s:
    f[c] += 1
while not palindromic(f, l):
    o = odds(f)
    if len(o) >= 1:
        f[o[0]] -= 1
    else:
        f[evens(f)[0]] -= 1
    l -= 1
print('First' if (len(s) - l) % 2 == 0 else 'Second')
