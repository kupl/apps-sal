def ni(): return int(input())
def nm(): return list(map(int, input().split()))
def nl(): return list(map(int, input().split()))


n = ni()
mins = []
maxs = []
for i in range(n):
    a, b = nm()
    mins.append(a)
    maxs.append(b)

smn = sorted(mins)
smx = sorted(maxs)

if n % 2 == 1:
    mn = smn[(n + 1) // 2 - 1]
    mx = smx[(n + 1) // 2 - 1]
    print((round((mx - mn) + 1)))
else:
    mn = (smn[n // 2 - 1] + smn[n // 2]) / 2.0
    mx = (smx[n // 2 - 1] + smx[n // 2]) / 2.0
    print((round((mx - mn) * 2 + 1)))
