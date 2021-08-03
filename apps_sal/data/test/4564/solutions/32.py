S = input()
ans = ""

for s in S:
    if S.count(s) > 1:
        ans = "no"
        break
    else:
        ans = "yes"

print(ans)
