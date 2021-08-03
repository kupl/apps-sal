def main(K):
    ans = -1
    if K % 2 == 0 or K % 5 == 0:
        return ans
    else:
        seven = 7
        for i in range(K):
            if seven % K == 0:
                ans = i + 1
                return ans
            seven = (seven * 10 + 7) % K


def __starting_point():
    K = int(input())
    ans = main(K)
    print(ans)


__starting_point()
