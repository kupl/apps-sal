n = int(input())
A = [int(x) for x in input().split()]
mx = max(A)
streak = 0
cur = 0
for a in A:
    if a == mx:
        cur += 1
        streak = max(streak, cur)
    else:
        cur = 0
print(streak)
