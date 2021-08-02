n = int(input())

ans = 0
if n % 4 == 0:
    ans = 0
elif n % 4 == 1:
    ans = 1
elif n % 4 == 2:
    ans = 1
elif n % 4 == 3:
    ans = 0

print(ans)
