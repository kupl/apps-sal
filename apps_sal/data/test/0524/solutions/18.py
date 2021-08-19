"""
NTC here
"""


def iin():
    return int(input())


def lin():
    return list(map(int, input().split()))


def main():
    T = 1
    for t in range(T):
        n = iin()
        a = lin()
        a.sort()
        ans = sum(a) - n
        for val in range(1, 100001):
            sm = 0
            ch = 1
            br = 0
            for i in a:
                sm += abs(ch - i)
                ch *= val
                if sm > ans:
                    br = 1
                    break
            else:
                ans = min(ans, sm)
            if br:
                break
        print(ans)


main()
'\n3\n4 1 3 1\n4 4 4 3\n5 3 3 2\n'
