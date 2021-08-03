s = sorted(input())
t = sorted(input(), reverse=True)
s = "".join(s)
t = "".join(t)
#print(s, t)
if s < t:
    print("Yes")
else:
    print("No")
