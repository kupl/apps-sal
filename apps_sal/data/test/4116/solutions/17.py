a = int(input())
f = False
for i in range(1,10):
    if a % i == 0 and a/i < 10:
        f = True
        break
if f:
    print("Yes")
else:
    print("No")
