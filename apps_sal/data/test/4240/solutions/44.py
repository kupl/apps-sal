s = [a for a in input()]
t = [b for b in input()]
temp = None
for _ in range(len(s)):
    if s == t:
        print("Yes")
        return
    temp = s.pop(0)
    s.append(temp)
print("No")
