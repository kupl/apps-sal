def woodenBarNum(n, a, b):
    remA = 4
    remB = 2
    numWood = 0
    remWood = 0
    for i in range(remA):
        if remWood < a:
            numWood += 1
            remWood = n
        remWood -= a
        if remWood >= b and remB > 0:
            remWood -= b
            remB -= 1
    if remB > 0:
        for j in range(remB):
            if remWood < b:
                numWood += 1
                remWood = n
            remWood -= b
    return numWood
n = int(input())
a = int(input())
b = int(input())
print(woodenBarNum(n,a,b))
