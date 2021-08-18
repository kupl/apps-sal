from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    s = input().rstrip()
    ans = []
    ans.append("
    for ch in s:
        ans.append(ch)
    ans.append("
    ok=True
    for i in range(1, len(ans) - 1):
        if ans[i] == ans[i + 1] and ans[i] != "?":
            ok=False
            break
        if ans[i] != "?":
            continue
        if "a" not in ans[i - 1] + ans[i + 1]:
            ans[i]="a"
        elif "b" not in ans[i - 1] + ans[i + 1]:
            ans[i]="b"
        elif "c" not in ans[i - 1] + ans[i + 1]:
            ans[i]="c"
    if ok:
        print("".join([item for item in ans[1:-1]]))
    else:
        print(-1)
