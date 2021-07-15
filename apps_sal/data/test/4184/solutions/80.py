n = int(input())
w = list(map(int,input().split()))
s = sum(w)
ans = int(100000000)
m = int(0)
for i in range(n):
    m += w[i]
    ans = min(ans,abs(2*m-s))
print(ans)
