n = str(input())
sum = 0
for i in range(0, len(n)):
    sum += int(n[i])
n = int(n)
if n % sum == 0:
    print("Yes")
else:
    print("No")
