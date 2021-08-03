a, b = input().split("e")
b = int(b)
c, d = a.split(".")
d += "0" * 500
ans = c + d[:int(b)] + "." + d[int(b):]
while ans[len(ans) - 1:] == "0":
    ans = ans[:len(ans) - 1]
if ans[len(ans) - 1:] == ".":
    ans = ans[:len(ans) - 1]
print(ans)
