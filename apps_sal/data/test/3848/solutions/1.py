import sys

n, p = map(int, input().split())
s = input()
a = [(ord(s[i]) - ord('a') + 1) for i in range(n)]
curr = len(s) - 1
a += [p + 1, p + 1]
f = 0


def valid(x):
    nonlocal f
    if x == -1:
        return False
    if not (a[x] + 1 in (a[x - 1], a[x - 2])) and a[x] + 1 <= p:
        a[x] += 1
    elif not (a[x] + 2 in (a[x - 1], a[x - 2])) and a[x] + 2 <= p:
        a[x] += 2
    elif not (a[x] + 3 in (a[x - 1], a[x - 2])) and a[x] + 3 <= p:
        a[x] += 3
    else:
        return True
    print(s[:x], end='')
    print(chr(a[x] + ord('a') - 1), end='')
    tmp = 1
    ind = x
    while tmp in (a[x], a[x - 1]):
        tmp += 1
    for i in range(x + 1, len(s)):
        print(chr(tmp + ord('a') - 1), end='')
        a[i] = tmp
        tmp = 1
        while tmp in (a[i], a[i - 1]):
            tmp += 1
    f = 1
    return False


while valid(curr):
    curr -= 1

if f == 1:
    return

print('NO')
