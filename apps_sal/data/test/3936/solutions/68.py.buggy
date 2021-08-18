import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

if N == 1:
    print(3)
    return

DIV = 1000000007

ind = 0
ans = 1
tate = False
if S[ind] == S[ind + 1]:
    ans *= 6
    ind += 2
    tate = False
else:
    ans *= 3
    ind += 1
    tate = True

while ind < N:
    if ind + 1 == N or S[ind] != S[ind + 1]:  # 縦
        if tate:
            ans *= 2
        else:
            ans *= 1
        ans %= DIV
        tate = True
        ind += 1
    else:  # 横
        if tate:
            ans *= 2
        else:
            ans *= 3
        ans %= DIV
        tate = False
        ind += 2

print(ans)
