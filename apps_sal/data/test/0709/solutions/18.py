a = int(input())
ans = 0
while a != 0:
    c = a % 2
    ans = ans + c
    a = a // 2
print(ans)
