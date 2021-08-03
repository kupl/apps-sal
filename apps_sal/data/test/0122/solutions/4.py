
# Python Interpreter Version: Python 3.5.2
#
# Note: Educational Codeforces Round 21

def divPos(arr):
    sumArr = sum(arr)
    targetSum = sumArr / 2
    if sumArr % 2 != 0:
        return False
    lArr = set()
    sumlArr = 0
    for i in range(len(arr)):
        lArr.add(arr[i])
        sumlArr += arr[i]
        if sumlArr == targetSum or (sumlArr > targetSum and sumlArr - targetSum in lArr):
            return True
    return False


def __starting_point():
    n = input()
    arr = [int(x) for x in input().split()]
    # arr = [2,2,3,4,5]
    if divPos(arr) or divPos(arr[::-1]):
        print('YES')
    else:
        print('NO')


__starting_point()
