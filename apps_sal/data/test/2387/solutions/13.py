import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
ls, rs = [], []
total = 0
for i in range(n):
    s = input()
    h, b = 0, 0
    for c in s:
        if c=='(':  h += 1
        else:       h -= 1
        b = min(b, h)
    if h > 0:   ls.append((b, h))       # 増減+ はb:最下点, h:増減を取る
    else:       rs.append((b-h, -h))    # 増減- は、上下左右逆さに考え、b:右から見た最下点、h:増減のマイナスを取る
    total += h
ls.sort(reverse=True)
rs.sort(reverse=True)   # 増減-は右から見るので、大きい順にsort

def chk(s):
    h = 0
    for sb, sh in s:
        b = h + sb
        if b < 0: return False
        h += sh
    return True

if (chk(ls) and chk(rs) and total==0):
    print("Yes")
else:
    print("No")
