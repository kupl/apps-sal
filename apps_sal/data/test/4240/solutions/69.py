s = input()
t = input()
s = list(s)
t = list(t)

count = 0
judgment = 0

while count <= len(s):
    item = s.pop()
    s.insert(0, item)
    if s == t:
        judgment += 1
    count += 1

if judgment == 0:
    print("No")
else:
    print("Yes")
