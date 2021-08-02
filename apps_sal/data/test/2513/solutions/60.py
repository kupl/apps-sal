import sys
N = int(input())
s = input()
List = [['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']]
for i in range(4):
    ans = List[i]
    for i in range(1, N):
        if i != N - 1:
            if (ans[i - 1] == ans[i] and s[i] == 'o') or (ans[i - 1] != ans[i] and s[i] == 'x'):
                ans.append('S')
            else:
                ans.append('W')
        else:
            if ((((ans[N - 1] == 'S' and s[N - 1] == 'o') or (ans[N - 1] == 'W' and s[N - 1] == 'x')) and (ans[N - 2] == ans[0])) or (((ans[N - 1] == 'S' and s[N - 1] == 'x') or (ans[N - 1] == 'W' and s[N - 1] == 'o')) and (ans[N - 2] != ans[0]))) and ((((ans[0] == 'S' and s[0] == 'o') or (ans[0] == 'W' and s[0] == 'x')) and (ans[N - 1] == ans[1])) or (((ans[0] == 'S' and s[0] == 'x') or (ans[0] == 'W' and s[0] == 'o')) and (ans[N - 1] != ans[1]))):
                print(''.join(ans))
                return
print(-1)
