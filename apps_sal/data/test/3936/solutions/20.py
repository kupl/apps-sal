N = int(input())
S1 = input()
S2 = input()
ans = 1
MOD = 10**9 + 7
i = 0
flag = True

while i < N:
    if S1[i] == S2[i]:
        if i == 0:
            ans *= 3
        else:
            if flag:
                ans *= 2

        i += 1
        flag = True
    else:
        if i == 0:
            ans *= 6
        else:
            if flag:
                ans *= 2
            else:
                ans *= 3

        i += 2
        flag = False

    ans %= MOD

print(ans)
