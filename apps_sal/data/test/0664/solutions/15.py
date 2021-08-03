import sys


def minindex(alist):
    index = -1
    min = 1000000
    for idx, num in enumerate(alist):
        if num < min:
            index = idx
            min = num
    return index


def isSorted(array):
    min = 0
    for num in array:
        if num < min:
            return False
        min = num
    return True


nums = int(sys.stdin.readline())

numbers = [int(num) for num in sys.stdin.readline().split()[0:nums]]

index = minindex(numbers)
min = numbers[index]


moves = 0
if index == 0:
    for num in range(nums - 1, -1, -1):
        if num == 0:
            moves = 0
            break
        if numbers[num] == min:
            moves = moves + 1
        else:
            break

    newnumbers = numbers[index:nums - moves]
    if isSorted(newnumbers):
        print(moves)
    else:
        print(-1)

else:
    newnumbers = numbers[index:]
    newnumbers.extend(numbers[0:index])
    if isSorted(newnumbers):
        print(nums - index)
    else:
        print(-1)
