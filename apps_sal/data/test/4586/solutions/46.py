s = input()
if len(set(s[:3])) == 1 or len(set(s[1:])) == 1:
    print("Yes")
else:
    print("No")
