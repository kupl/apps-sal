n = int(input())
S = input()
ans = ""
for s in S:
    if ans == "" or ans[-1] != s: ans += s
print(len(ans))
