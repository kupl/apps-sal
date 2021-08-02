s = input()
t = input()
k = 0
for i in range(len(s)):
    x = s[i:] + s[:i]
    if x == t:
        k = 1
        break
if k == 1:
    print("Yes")
else:
    print("No")
