def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def __starting_point():
    n = int(input())
    A = list(map(int, input().split()))
    ans, cnt = [A[0]], 0
    for i in range(1, n):
        if gcd(A[i], A[i - 1]) != 1:
            ans.append(1)
            cnt += 1
        ans.append(A[i])
    print(cnt)
    print(' '.join(str(i) for i in ans))


__starting_point()
