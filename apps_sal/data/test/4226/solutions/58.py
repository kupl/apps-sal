X, Y = list(map(int, input().split()))
for i in range(100):
    for j in range(100):
        if i + j == X and 2 * i + 4 * j == Y:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")
