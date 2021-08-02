s = list(input())
t = list(input())
num = len(s) - len(t)
ans1 = -1
for i in range(num + 1):
    num1 = 0
    num2 = num - i
    for j in range(len(t)):
        if s[num2 + j] != t[j] and s[num2 + j] != "?":
            num1 = 1
            break
    if num1 == 0:
        ans1 = num2
        break
if ans1 == -1:
    print("UNRESTORABLE")
else:
    ans = ""
    for i in range(len(t)):
        s[ans1 + i] = t[i]
    for i in range(len(s)):
        if s[i] == "?":
            s[i] = "a"
        ans += s[i]
    print(ans)
