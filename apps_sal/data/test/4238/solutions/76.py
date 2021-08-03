x = input()

sum = 0
for i in x:
    sum = sum + int(i)

if sum % 9 == 0:
    print("Yes")
else:
    print("No")
