# N = 15
# ARR = [1, 3, 5, 2, 1, 3, 2, 8, 8, 6, 2, 6, 11, 1, 1]

# N = 5
# ARR = [1, 2, 1, 3, 7]

N = int(input())
ARR = list(map(int, input().split()))


def calculate(n, arr):
    dict = {}
    for i in range(n):
        if dict.get(arr[i]) == None:
            dict.__setitem__(arr[i], 1)
        else:
            tmp = dict.get(arr[i])
            dict.__setitem__(arr[i], tmp + 1)

    k1 = len(list(dict.keys()))

    if k1 % 2 == 0:
        print((k1 - 1))
    else:
        print(k1)


calculate(N, ARR)
