a, b = list(map(int, input().split()))

if (any([(i * a * b) % 2 != 0 for i in range(1, 4)])) :
    print("Yes")
else :
    print("No")

