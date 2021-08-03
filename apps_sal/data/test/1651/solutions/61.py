import math


def main():

    s, p = list(map(int, input().split()))
    try:
        ans_1 = math.floor(s + math.sqrt(s**2 - 4 * p)) // 2
    except:
        print("No")
        return

    for _ in range(-1, 2):

        ans_2 = s - ans_1

        if ans_2 > 0 and ans_1 * ans_2 == p:
            print("Yes")
            return

    print("No")
    return


main()
