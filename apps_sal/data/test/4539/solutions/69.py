n = input()
f_x = 0
for i in range(len(n)):
    f_x += int(n[i])
if int(n) % f_x == 0:
    print("Yes")
else:
    print("No")
