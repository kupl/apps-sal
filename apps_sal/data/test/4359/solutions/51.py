a = input()
b = input()
c = input()
d = input()
e = input()
li = []

li.append(10 - int(a[-1]))
li.append(10 - int(b[-1]))
li.append(10 - int(c[-1]))
li.append(10 - int(d[-1]))
li.append(10 - int(e[-1]))

while 10 in li: li.remove(10)

li.sort()
n = len(li)
if n != 0:
    li.pop(n - 1)

print(int(a) + int(b) + int(c) + int(d) + int(e) + sum(li))
