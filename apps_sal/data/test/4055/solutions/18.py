from collections import Counter


def solution(n, a):

    count = 0
    ind = 1
    while(ind < n - 1):
        if(a[ind] == 0 and a[ind - 1] == 1 and a[ind + 1] == 1):
            a[ind + 1] = 0
            ind = 1
            count += 1
        ind += 1
    print(count)


def __starting_point():

    n = [int(val) for val in input().split()][0]

    arr = [int(val) for val in input().split()]

    solution(n, arr)


__starting_point()
