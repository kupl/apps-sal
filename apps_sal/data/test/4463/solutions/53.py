s = sorted(list(input()))
t = sorted(list(input()), reverse=True)
for i in range(min(len(s), len(t))):
    if ord(s[i]) < ord(t[i]):
        print("Yes")
        return
    elif ord(s[i]) > ord(t[i]):
        print("No")
        return
if len(s) >= len(t):
    print("No")
else:
    print("Yes")
