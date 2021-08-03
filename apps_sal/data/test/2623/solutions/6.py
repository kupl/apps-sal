import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input().rstrip())
    s.sort()
    if len(set(s[:k])) > 1:
        print(max(s[:k]))
        continue
    ss = s[k:]
    if len(set(ss)) == 1:
        print(s[0], *([ss[0]] * ((len(ss) - 1) // k + 1)), sep="")
    else:
        print(s[0], *s[k:], sep="")
