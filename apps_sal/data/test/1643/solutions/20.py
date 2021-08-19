def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


def inm():
    return list(map(int, input().split()))


DBG = True and False


def ddprint(x):
    if DBG:
        print(x)


s = input().strip()
n = len(s)
ones = []
stk = []
for i in range(n):
    if len(stk) > 0 and stk[-1][0] == '1' and (s[i] == '0'):
        ones.append(stk[-1][1])
        stk.pop()
    else:
        stk.append((s[i], i))
ones.sort()
ans = ''
cur = 0
for i in ones:
    for j in range(cur, i):
        ans += '0'
    ans += '1'
    cur = i + 1
for j in range(cur, n):
    ans += '0'
print(ans)
