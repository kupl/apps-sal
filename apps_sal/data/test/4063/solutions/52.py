N = int(input())
d = list(map(int,input().split()))
d.sort()
dmed1 = N//2 - 1
dmed2 = N//2
ans = d[dmed2]-d[dmed1]
print(ans)
