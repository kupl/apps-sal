N = int(input())
S1 = input()
S2 = input()
ans = 0
tate = True

if S1[0] == S2[0]:
    ans = 3
    tate = True
    i = 1
else:
    ans = 6
    tate = False
    i = 2

while i < N:
    if S1[i] == S2[i]:
        if tate:
            ans *= 2
        i += 1
        tate = True

    else:
        if tate:
            ans *= 2
        else:
            ans *= 3
        i += 2
        tate = False

    ans %= 1000000007

print(ans)
