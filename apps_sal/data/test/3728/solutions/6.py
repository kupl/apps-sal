from copy import deepcopy

n, m = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


def solve(arr):
    for row in arr:
        count = 0
        for i, num in enumerate(row):
            if i + 1 != num:
                count += 1
                if count > 2:
                    return False
    return True


def permute(arr, i, j):
    arr_ = deepcopy(arr)
    for k in range(n):
        arr_[k][i], arr_[k][j] = arr_[k][j], arr_[k][i]
    return arr_


def main():
    if solve(arr):
        print("YES")
        return

    for row in arr:
        wrong_cols = []
        for i, num in enumerate(row):
            if i + 1 != num:
                wrong_cols.append(i)
        if wrong_cols:
            if len(wrong_cols) > 4:
                print("NO")
                return
            for col in wrong_cols:
                if solve(permute(arr, col, row[col] - 1)):
                    print("YES")
                    return
            print("NO")
            return

    print("NO")
    return


main()
