s = input()
t = input()
if s < t:
    print("Yes")
    return
s = list(s)
t = list(t)
s = sorted(s)
t = sorted(t)
t = t[::-1]
s = ''.join(s)
t = ''.join(t)
if s < t:
    print("Yes")
else:
    print("No")
