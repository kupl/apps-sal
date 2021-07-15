n = input()
f_n = 0
for i in n: f_n += int(i)
if int(n) % f_n == 0: print("Yes")
else: print("No")
