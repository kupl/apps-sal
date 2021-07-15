a, b = input().split()

a = int(a)
b1, b2 = b.split('.')

ans = a * (int(b1) * 100 + int(b2)) // 100
print(ans)
