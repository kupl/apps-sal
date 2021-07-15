s = sorted(list(input()))
t = reversed(sorted(list(input())))
if ",".join(s) < ",".join(t):
    print("Yes")
else:
    print("No")
