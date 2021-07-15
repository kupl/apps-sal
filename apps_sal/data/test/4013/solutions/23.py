#codeforces _1095B_live
gi = lambda : list(map(int,input().split()))
n, = gi()
l = gi()
l.sort()
ans = min(max(l)-min(l[1:]),(max(l[:-1])-min(l)))
print(ans)

