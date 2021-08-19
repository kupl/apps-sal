a = int(input())
for i in range(a):
    b = int(input())
    for j in range(2 * b + 2, 4 * b, 2):
        print(j, end=' ')
    print(4 * b)
