
n = str(input())

a = 0

for i in range(len(n)):
    a += int(n[i])

if int(n) % a == 0:
    print("Yes")
else:
    print("No")
