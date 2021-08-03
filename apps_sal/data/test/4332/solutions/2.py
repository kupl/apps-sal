n = input()
c = 0
for i in range(len(n)):
    c += int(n[i])

if int(n) % c == 0:
    print("Yes")
else:
    print("No")
