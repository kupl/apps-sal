s = input()
t = input()
ans = 0
for i in range(len(s)):
    s = s[-1]+s[:-1]
    if s == t:
        ans = 1
print("Yes" if ans==1 else "No")
