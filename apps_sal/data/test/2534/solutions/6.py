# cook your dish here


"""


"""


def check_in_column(arr, value, index, X):
    for i in range(X):
        if arr[i][index] > value:
            return False
    return True


def result(arr, X, Y):
    for i in range(X):
        s = min(arr[i])
        for j in range(Y):
            if (arr[i][j] == s):
                if(check_in_column(arr, s, j, X)):
                    return s
    return "GUESS"


X, Y = [int(d) for d in input().split()]
arr = []
for i in range(X):
    arr.append([int(d) for d in input().split()])


print(result(arr, X, Y))
