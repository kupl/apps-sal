import sys

input = sys.stdin.readline

t = int(input())

for zzz in range(t):
    l = int(input())
    s = input().strip()
    good = True
    for i in range(l):
        j = l - i - 1
        diff = abs(ord(s[i]) - ord(s[j]))
        if (diff == 1 or diff > 2):
            good = False
            break
    if good:
        print('YES')
    else:
        print('NO')
