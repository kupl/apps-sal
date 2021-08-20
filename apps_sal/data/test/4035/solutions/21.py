(A, B) = map(int, input().split())
b = 10 * B
if b * 2 // 25 == A:
    print(b)
elif (b + 9) * 2 // 25 == A:
    if A % 2 == 0:
        print(A * 25 // 2)
    else:
        print((A * 25 + 1) // 2)
else:
    print(-1)
