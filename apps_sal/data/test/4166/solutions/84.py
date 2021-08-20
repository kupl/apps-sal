import sys


def generate_2d_array(Row, Column, IV):
    array = [[IV] * Row for i in range(Column)]
    return array


'\ndef search_in_2d_array(array, Row, Column, V):\n    cnt = 0\n    for i in range(Column):\n        for j in range(Row):\n            if array[i][j] == V:\n                cnt += 1\n    return cnt\n'


def input_2d_array(Row, Column):
    array = generate_2d_array(Row, Column, 0)
    for i in range(Column):
        temp = list(map(int, input().split()))
        for j in range(Row):
            array[i][j] = temp[j]
    return array


def __starting_point():
    (N, M) = map(int, input().split())
    sc = input_2d_array(2, M)
    if M == 0 and N != 1:
        print(10 ** (N - 1))
        return
    'if N == 1:\n        flag = True\n        for i in reversed(range(10)):\n            for j in range(M):\n                if i == sc[j][1] and flag:\n                    flag = True\n                else:\n                    flag =False\n\n            if flag == True and M != 0:\n                print(sc[0][1])\n                return\n            else:\n                print(-1)\n                return\n\n        print(0)\n        return'
    if N == 1:
        if M > 1:
            print(-1)
            return
        for i in range(10):
            for j in range(M):
                if i == sc[j][1]:
                    print(i)
                    return
        print(0)
        return
    ans = -1
    flag = True
    for i in reversed(range(10 ** (N - 1), 10 ** N)):
        for j in range(M):
            temp = str(i)
            if str(sc[j][1]) == temp[sc[j][0] - 1] and flag:
                flag = True
            else:
                flag = False
        if flag:
            ans = int(temp)
        flag = True
    print(ans)


__starting_point()
