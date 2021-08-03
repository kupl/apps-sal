n = int(input())  # always odd
# takes the shape of an expanding cross
evenNums = list(range(2, n**2 + 1, 2))
oddNums = list(range(1, n**2 + 1, 2))
for i in range(n):
    outList = []
    if i > n // 2:
        oddNumIndeces = (list(range(n // 2 + i - n + 1, n // 2 - (i - n))))
    else:
        oddNumIndeces = list(range(n // 2 - i, n // 2 + i + 1))
    for j in range(n):

        if j not in oddNumIndeces:
            outList.append(str(evenNums[0]))
            evenNums.pop(0)
        else:
            outList.append(str(oddNums[0]))
            oddNums.pop(0)

    print(" ".join(outList))
