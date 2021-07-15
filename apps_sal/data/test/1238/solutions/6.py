#codeforces_1041A_live
gi = lambda : list(map(int,input().split()))
n, = gi()
l = gi()
print(max(l)-min(l)+1-len(l))
