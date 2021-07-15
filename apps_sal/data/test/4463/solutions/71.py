s = input()
t = input()

if "".join(sorted(s)) < "".join(list(reversed(sorted(t)))):
    print("Yes")
else:
    print("No")

