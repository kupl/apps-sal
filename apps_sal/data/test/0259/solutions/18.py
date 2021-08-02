import math


def main():
    n, t = list(map(int, input().split()))
    buses = []
    min_ans = float('inf')
    index = -1
    for i in range(n):
        s, d = list(map(int, input().split()))
        if s >= t:
            k = 0
        else:
            k = math.ceil((t - s) / d)
        wait = s + (k * d)
        ans = wait - t
        if ans < min_ans:
            min_ans = ans
            index = i + 1

    print(index)


main()
