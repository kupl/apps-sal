s = input()
sum = 0
for i in s:
    sum+=int(i)
if int(s)%sum == 0: print("Yes")
else: print("No")
