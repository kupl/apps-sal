N = int(input())
S = input()
lsS = list(S)
lscount = [lsS.count('R'), lsS.count('G'), lsS.count('B')]
ans = 1
for i in lscount:
    ans *= i
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if lsS[i] == lsS[j]:
            continue
        if 2 * j - i <= N - 1:
            if lsS[i] != lsS[2 * j - i] and lsS[j] != lsS[2 * j - i]:
                ans -= 1
        else:
            break
print(ans)
