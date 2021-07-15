n = int(input())
s = input().split("0")
ans = ""
for a in s:
    if a == "":
        ans = ans + str(0)
    else:
        ans = ans + str(len(a))
print(ans)
