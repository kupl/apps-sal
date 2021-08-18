from bisect import bisect_left
from functools import cmp_to_key
def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)
def printlist(l): print(''.join([str(x) for x in l]))
def listring(l): return ''.join([str(x) for x in l])


s = input()
t = input()
s_rev = s[::-1]


def check(st, substr):
    index = 0
    if substr in st:
        c = substr[0]
        while index < len(st) - len(substr) + 1:
            if st[index] == c:
                if st[index:index + len(substr)] == substr:
                    return index
            index += 1
    return -1


pos = 0
L = []
while pos < len(t):
    substr = t[pos:pos + 1]
    if substr not in s and substr not in s_rev:
        print(-1)
        return
    index = 1
    while t[pos:pos + index] in s or t[pos:pos + index] in s_rev:
        index += 1
        if pos + index > len(t):
            break
    index -= 1
    substr = t[pos:pos + index]
    if check(s, substr) == -1:
        start = len(s) - 1 - check(s_rev, substr)
        end = start - index + 1
    else:
        start = check(s, substr)
        end = start + index - 1
    L.append((start + 1, end + 1))
    pos += index

print(len(L))
for i in L:
    print("%d %d" % (i[0], i[1]))
