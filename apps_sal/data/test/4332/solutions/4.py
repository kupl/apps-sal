n = str(input())
s = 0
for i in range(len(n)):
    s += int(n[i])

n = int(n)
if n % s == 0:
    print("Yes")
else:
    print("No")
