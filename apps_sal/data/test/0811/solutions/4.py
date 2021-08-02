a, b = list(map(int, input().split()))
ans = a
while a >= b:
    f = a // b
    ans += f
    a = a % b + f
print(ans)
