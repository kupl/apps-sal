n = input()
sn = 0
for i in range(0, len(n)):
    sn += int(n[i])
if int(n) % sn == 0: print("Yes")
else: print("No")
