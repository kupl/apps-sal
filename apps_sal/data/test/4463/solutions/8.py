s = "".join(sorted(input()))
t = "".join(sorted(input(), reverse=True))
if s < t:
    print("Yes")
else:
    print("No")
