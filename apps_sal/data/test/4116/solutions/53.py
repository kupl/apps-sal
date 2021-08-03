n = int(input())
ans = 0
for i in range(1, 10):
    if n % i == 0 and n / i < 10:
        ans = 1
if ans == 0:
    print("No")
else:
    print("Yes")
