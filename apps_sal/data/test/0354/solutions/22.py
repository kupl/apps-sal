s = input()
t = input()
v = ["a", "i", "u", "e", "o"]
flag = True
if len(s) != len(t):
    print("No")
else:
    for i in range(len(s)):
        if not ((s[i] in v and t[i] in v) or (s[i] not in v and t[i] not in v)):
            flag = False

    if flag:
        print("Yes")
    else:
        print("No")
