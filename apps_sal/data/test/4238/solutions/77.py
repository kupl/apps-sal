n = list(input())
x = 0

for i in n:
    x += int(i)

if x % 9 == 0:
    print("Yes")
else:
    print("No")
