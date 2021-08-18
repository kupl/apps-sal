a, b = list(map(int, input().split()))


if a == 1 and b == 0:
    print("0 0")
    return
if b == 0 or b > a * 9:
    print("-1 -1")
    return

ob = b
ans = ""
for x in range(a):
    if ob > 9:
        ob -= 9
        ans += "9"
    else:
        ans += str(ob)
        ob = 0
big = ans
ans = ""

ob = b
ob -= 1
for x in range(a):
    if ob > 9:
        ob -= 9
        ans = "9" + ans
    else:
        ans = str(ob) + ans
        ob = 0

ans = chr(ord(ans[0]) + 1) + ans[1:]
print(ans, big)
