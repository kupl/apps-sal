n = int(input())
for i in range(n):
    k = int(input())
    if k < 4:
        print(4 - k)
    else:
        print(k % 2)
