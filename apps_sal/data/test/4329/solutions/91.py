s = input()
t = input()

ans_bool = True
for i in range(len(s)):
    if s[i] != t[i]:
        ans_bool = False
        break

if ans_bool:
    print("Yes")
else:
    print("No")
