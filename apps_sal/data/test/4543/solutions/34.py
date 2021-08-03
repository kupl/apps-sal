a, b = list(input().split())
num = int(a + b)
ans = round(num**0.5)
if ans**2 == num:
    print("Yes")
else:
    print("No")
