s = input()
l = len(s)
if s[l - 1] == "s":
    ans = s + "es"
else:
    ans = s + "s"
print(ans)
