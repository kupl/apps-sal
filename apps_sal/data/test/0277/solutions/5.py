(n, a, b) = map(int, input().split())
ans = 0
a -= 1
b -= 1
while n > 2:
    n //= 2
    a //= 2
    b //= 2
    ans += 1
    if a == b:
        print(ans)
        break
else:
    print('Final!')
