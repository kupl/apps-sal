n = input()
x = int(n)
s = 0
for i in range(len(n)):
    s += int(n[i])
if x%s == 0:
    print("Yes")
else:
    print("No")
