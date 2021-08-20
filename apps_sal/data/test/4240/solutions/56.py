S = input()
T = input()
ans = T
for i in range(len(S)):
    ans = ans[-1] + ans[:-1]
    if S == ans:
        print('Yes')
        break
else:
    print('No')
