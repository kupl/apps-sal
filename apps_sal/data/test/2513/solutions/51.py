N = int(input())
s = input()

# 1番目を決めると全て決まる→これは間違った性質
# 正しくはある連続した2匹の動物の種類がわかれば、その隣にいる動物の種類もわかるということ

pattern = [['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']]

L = []
for i in range(4):
    ans = ''
    for j in range(N):
        if j == 0:
            ans += pattern[i][j]
            continue
        if j == 1:
            ans += pattern[i][j]
            continue

        if s[j -
             2] == 'o' and s[j -
                             1] == 'o' and ans[j -
                                               1] == 'S' and ans[j -
                                                                 2] == 'S':
            ans += 'S'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'S':
            ans += 'S'
        elif s[j -
               2] == 'o' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'S':
            ans += 'W'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'S':
            ans += 'W'

        elif s[j -
               2] == 'o' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'W':
            ans += 'W'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'W':
            ans += 'W'
        elif s[j -
               2] == 'o' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'W':
            ans += 'S'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'S' and ans[j -
                                                                   2] == 'W':
            ans += 'S'

        elif s[j -
               2] == 'o' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'S':
            ans += 'W'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'S':
            ans += 'W'
        elif s[j -
               2] == 'o' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'S':
            ans += 'S'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'S':
            ans += 'S'

        elif s[j -
               2] == 'o' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'W':
            ans += 'S'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'o' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'W':
            ans += 'S'
        elif s[j -
               2] == 'o' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'W':
            ans += 'W'
        elif s[j -
               2] == 'x' and s[j -
                               1] == 'x' and ans[j -
                                                 1] == 'W' and ans[j -
                                                                   2] == 'W':
            ans += 'W'

    if ans[-1] == 'S' and s[-1] == 'o' and ans[0] != ans[-2]:
        continue
    if ans[-1] == 'S' and s[-1] == 'x' and ans[0] == ans[-2]:
        continue
    if ans[-1] == 'W' and s[-1] == 'o' and ans[0] == ans[-2]:
        continue
    if ans[-1] == 'W' and s[-1] == 'x' and ans[0] != ans[-2]:
        continue

    if ans[0] == 'S' and s[0] == 'o' and ans[-1] != ans[1]:
        continue
    if ans[0] == 'S' and s[0] == 'x' and ans[-1] == ans[1]:
        continue
    if ans[0] == 'W' and s[0] == 'o' and ans[-1] == ans[1]:
        continue
    if ans[0] == 'W' and s[0] == 'x' and ans[-1] != ans[1]:
        continue

    L.append(ans)

if len(L) != 0:
    print((L[0]))
else:
    print((-1))

