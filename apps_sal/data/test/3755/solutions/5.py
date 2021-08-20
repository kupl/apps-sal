def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    even = sum([max(A[i], 0) for i in range(0, N, 2)])
    odd = sum([max(A[i], 0) for i in range(1, N, 2)])
    if even == odd == 0:
        a = max(A)
        print(a)
        print(N - 1)
        flg = 1
        for i in range(N - 1):
            if A[i] == a:
                flg = 0
            if flg:
                print(1)
            else:
                print(N - i)
        return
    ans = []
    i = 0
    if odd > even:
        if N % 2 == 1:
            ans.append(N)
            N -= 1
        ans.append(1)
        i = 1
    elif N % 2 == 0:
        ans.append(N)
        N -= 1
    flg = 1
    while True:
        if flg:
            if A[i] > 0:
                flg = 0
            else:
                ans.append(1)
                i += 1
                if i == N:
                    break
                ans.append(1)
                i += 1
                if i == N:
                    break
        else:
            if A[i + 2] > 0:
                ans.append(2)
                i += 2
            else:
                ans.append(3)
                i += 2
            if i + 2 >= N:
                break
    if ans[-1] == 3:
        ans.append(2)
    print(max(odd, even))
    print(len(ans))
    for x in ans:
        print(x)


def __starting_point():
    main()


__starting_point()
