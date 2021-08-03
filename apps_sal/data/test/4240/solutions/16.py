s = input()
t = input()

s_num = len(s)
i = 0
a = 0
while i < s_num:
    if s == t:
        a = 1
    s = s[-1] + s[0:s_num - 1]
    i = i + 1

if a == 1:
    print("Yes")
else:
    print("No")
