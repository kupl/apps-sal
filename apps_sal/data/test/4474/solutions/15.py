
arr = []
for i in range(40):
    arr.append(3**i)

n = int(input())
for i in range(n):
    sb = [0] * 40
    a = int(input())
    x = a
    xx = a
    for j in range(39, -1, -1):
        if(a - arr[j] >= 0):
            a -= arr[j]
            sb[j] = 1
    x = x - a
    if(a == 0):
        print(x)
        continue
    for j in range(40):
        if(sb[j] == 0):
            x = x + 3**j
            break
        else:
            x = x - 3**j
    print(x)
