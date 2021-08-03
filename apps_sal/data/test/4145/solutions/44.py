X = int(input())
if(X == 2):
    print(2)
    return
for i in range(X, 10**5 + 4):
    count = 0
    for j in range(2, int(i**0.5) + 2):
        if(i % j == 0):
            count += 1
            continue
        if(count == 0 and j == int(i**0.5) + 1):
            print(i)
            return
    count = 0
