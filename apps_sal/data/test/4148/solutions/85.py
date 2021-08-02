N = int(input())
S = input()
ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for s in S:
    ans += ss[ss.index(s) + N]
print(ans)
