N = int(input())
n = N
S = "abcdefghijklmnopqrstuvwxyz"
ans = ""
keta = 1
tw = []
r = 26
l = 1
i = 2
tw.append(l)

while 1:
    if l <= N <= r:
        break
    l, r = r+1, r+26**i
    tw.append(l)
    i += 1
    keta += 1
#print(l,r,keta,tw)

for x in tw[::-1]:
    twp = 26**(keta-1)
    keta -= 1
    #print("twp =",twp,"x =",x)
    a = (N - x) // twp
    #print((N - x) // twp)
    N -= twp*(a+1)
    ans += S[a]
    #print(N)
print(ans)
