K = int(input())

if K % 2 == 1:
    print((K // 2) * (K // 2 + 1))
else:
    print((K // 2)**2)
