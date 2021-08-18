N = int(input())
c1 = str(input())
c2 = str(input())
c3 = str(input())
c4 = str(input())

c = c1 + c2 + c3 + c4

if c in ["AAAA", "AAAB", "AABA", "AABB", "ABAB", "BBAB", "ABBB", "BBBB"]:
    print((1))

if c in ["ABAA", "BABA", "BABB", "BBAA"]:
    if N == 2 or N == 3:
        print((1))
    else:
        ans = 1
        for dummy in range(N - 3):
            ans *= 2
            ans = ans % (10**9 + 7)

        print(ans)

if c in ["BAAA", "BAAB", "ABBA", "BBBA"]:
    ans = [1, 1]
    if N == 2 or N == 3:
        print((1))
    else:
        for dummy in range(N - 3):
            ans += [(ans[-1] + ans[-2]) % (10**9 + 7)]

        print((ans[-1]))
