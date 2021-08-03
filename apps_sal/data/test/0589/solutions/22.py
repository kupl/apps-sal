def readln(): return tuple(map(int, input().split()))


ans = 1
cnt = set()
for i, c in enumerate(list(input())):
    if c == '?':
        ans *= 10 - (i == 0)
    elif c.isalpha() and c not in cnt:
        ans *= 10 - len(cnt) - (i == 0)
        cnt.add(c)
print(ans)
