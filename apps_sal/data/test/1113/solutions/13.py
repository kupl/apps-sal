import collections


def main():

    n = int(input())
    num = list(map(int, input().split()))
    prevMax, totMax = -1, float('-inf')
    for i, v in enumerate(num):
        totMax = max(totMax, v)
        if totMax - prevMax in [0, 1]:
            prevMax = totMax
        else:
            print(i + 1)
            return
    print(-1)


main()
