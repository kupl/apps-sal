s = input()
t = input()

s = list(s)
t = list(t)
s.sort()
t.sort(reverse=True)

s = "".join(s)
t = "".join(t)

print("Yes") if s < t else print("No")
