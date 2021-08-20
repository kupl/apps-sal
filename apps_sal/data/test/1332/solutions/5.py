(a, b, c, d, e) = map(int, input().split())
sum = a + b + c + d + e
if sum > 0 and sum % 5 == 0:
    print(sum // 5)
else:
    print(-1)
