n,m = map(int,input().split())
x_l = list(map(int, input().split()))
x_l = sorted(x_l)
sub_l = sorted([ x_l[i+1] - x_l[i] for i in range(m-1)])
if n >= m:
    ans = 0
else:
    r = m-n
    ans = sum(sub_l[:r])
print(ans)
