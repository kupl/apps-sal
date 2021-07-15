a, b, k = list(map(int, input().split()))

mylist = []

if a > b:
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            mylist.append(i)
else:
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            mylist.append(i)

print((mylist[-k]))

