x = int(input())

p = (x + 11 - 1) // 11
q = (x + 11 - 1) % 11
if q < 6:
    ans = p * 2 - 1
else:
    ans = p * 2

print(ans)
