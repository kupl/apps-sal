import sys
T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split()))
    ans = [p[0]]
    for i in range(1, n):
        if p[i] != ans[-1]:
            if len(ans) == 1:
                ans.append(p[i])
            else:
                if (ans[-2] - ans[-1]) * (ans[-1] - p[i]) > 0:
                    ans.pop()
                ans.append(p[i])
    print(len(ans))
    print(' '.join(list(map(str, ans))))
