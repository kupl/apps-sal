n, k = list(map(int, input().split()))
line = input()
j = k - 1
if n - k > k - 1:
    for i in range(k - 1):
        print("LEFT")
        j -= 1
    add = "RIGHT"
else:
    for i in range(n - k):
        print("RIGHT")
        j += 1
    add = "LEFT"
if j == 0:
    for i in range(n - 1):
        print("PRINT", line[i])
        print(add)
    print("PRINT", line[-1])
else:
    for i in range(j, 0, -1):
        print("PRINT", line[i])
        print(add)
    print("PRINT", line[0])

