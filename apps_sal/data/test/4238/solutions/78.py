n = input()
s = 0
for i in n:
    s += int(i)
if s % 9 == 0:
    print("Yes")
else:
    print("No")
