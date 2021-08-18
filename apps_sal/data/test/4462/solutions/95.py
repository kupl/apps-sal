n = int(input())
a = list(map(int, input().split()))

num4 = 0
num2 = 0
for i in range(n):
    if a[i] % 4 == 0:
        num4 += 1
    elif a[i] % 2 == 0:
        num2 += 1


if n - num4 * 2 <= 1:
    print("Yes")
elif n - num4 * 2 <= num2:
    print("Yes")
else:
    print("No")
