a, b = map(int, input().split())

ans = 0 
while True:
    if a == 0 or b == 0:
        break

    if a < b:
        a,b = b, a

    ans += a//b
    a = a % b

print(ans)
