N = int(input())
L = [64, 32, 16, 8, 4, 2]
for i in L:
    if i <= N:
        print(i)
        break
else:
    print(N)
