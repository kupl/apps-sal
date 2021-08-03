3

s = "CODEFORCES"

inp = input()

ans = False

for i in range(len(inp)):
    for j in range(i, len(inp) + 1):
        new_s = inp[:i] + inp[j:]
        if new_s == s:
            ans = True

if ans:
    print("YES")
else:
    print("NO")
