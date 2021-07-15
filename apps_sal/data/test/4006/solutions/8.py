n = int(input())
doneNums = []
while n not in doneNums:
    doneNums.append(n)
    n += 1
    while n % 10 == 0:
        n/=10
print(len(doneNums))
