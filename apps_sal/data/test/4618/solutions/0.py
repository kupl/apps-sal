import sys
stdin = sys.stdin


def ip(): return int(sp())
def fp(): return float(sp())
def lp(): return list(map(int, stdin.readline().split()))
def sp(): return stdin.readline().rstrip()
def yp(): return print('Yes')
def np(): return print('No')


s = list(sp())
k = ip()

ans = set()

alpa = list(set(s))
alpa.sort()
ch = 0
siyou = []
for i in range(len(alpa)):
    if i <= 2:
        siyou.append(alpa[i])
    else:
        break

for x in siyou:
    for i in range(len(s)):
        if s[i] == x:
            st = ''
            for y in range(i, i + 5):
                if y < len(s):
                    st += s[y]
                    ans.add(st)
    if len(ans) > k:
        break

ans = list(ans)
ans.sort()
print(ans[k - 1])
