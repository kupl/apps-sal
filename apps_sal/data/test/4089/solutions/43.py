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
    l, r = r + 1, r + 26**i
    tw.append(l)
    i += 1
    keta += 1

for x in tw[::-1]:
    twp = 26**(keta - 1)
    keta -= 1
    a = (N - x) // twp
    N -= twp * (a + 1)
    ans += S[a]
print(ans)
