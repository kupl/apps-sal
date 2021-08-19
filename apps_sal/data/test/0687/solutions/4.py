(a, b) = list(map(int, input().split()))
if a + 1 == b:
    print(a, b)
elif a == b:
    print(a * 10, b * 10 + 1)
elif a == 9 and b == 1:
    print(9, 10)
else:
    print(-1)
