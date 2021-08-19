t = int(input())
for nt in range(t):
    x = input()
    y = input()
    count = 0
    for i in range(len(y) - 1, -1, -1):
        if y[i] == '0':
            count += 1
        else:
            break
    k = 0
    for i in range(len(x) - 1 - count, -1, -1):
        if x[i] == '1':
            break
        else:
            k += 1
    print(k)
