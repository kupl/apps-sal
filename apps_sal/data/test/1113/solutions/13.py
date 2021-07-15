import collections


def main():
    # # n = int(input())
    # x, y, z, t1, t2, t3 = list(map(int, input().split()))
    # stair = t1 * abs(y - x)
    # ele = t2 * (abs(y - x) + abs(z - x)) + 3 * t3
    # # print(stair, ele)
    # print("YES" if ele <= stair else "NO")

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

