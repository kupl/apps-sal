(a, b) = list(map(int, input().split()))
ans = 0
while a >= b:
    ans = ans + b
    a = a - b + 1
print(ans + a)
