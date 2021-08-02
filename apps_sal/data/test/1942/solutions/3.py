import sys
input = sys.stdin.readline

T = int(input())
for tests in range(T):
    n, l, r = list(map(int, input().split()))

    begin = 1
    while l > (n - begin) * 2 + 1:
        if begin == n:
            break

        l -= (n - begin) * 2
        r -= (n - begin) * 2
        begin += 1

    # print(begin,l,r)

    if begin == n:
        ANS = [n, 1]
    else:

        ANS = []
        while len(ANS) <= r:
            if begin == n:
                ANS.append(1)
                break

            for j in range(begin + 1, n + 1):
                ANS.append(begin)
                ANS.append(j)
            begin += 1

            # print(ANS)

    print(*ANS[l - 1:r])
