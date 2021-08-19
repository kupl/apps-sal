

"""
N <= 5 * 10**3　なので、２重ループぐらいなら間に合うか？

例３
strangeorange
**range*range

他に２回以上出てくるものとして
r,a, みたいな単体
ra, nge みたいな最長の部分文字列の一部
みたいな感じなので
l,r (r=l+1~N-1)を持っておいて、S[l:r+1] = S[r+1:XX]になるものがあればさらに右をみて～みたいな？

"""


N = int(input())
S = input()


l = 0
r = 1
ans = 0
while True:
    if l == N - 1:
        break
    while S[l:r] in S[r:]:
        r += 1

    ans = max(ans, r - l - 1)
    #print(l,r, S[l:r], S[r:], ans)
    l += 1
    if l == r:
        r = l + 1

print(ans)
