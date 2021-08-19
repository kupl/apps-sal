def main():
    (x, k) = map(int, input().split())
    A = [0] * x
    mx = x - 1
    for i in range(k):
        s = list(map(int, input().split()))
        A[s[1] - 1] = 1
        if len(s) == 3:
            A[s[2] - 1] = 1
        mx -= len(s) - 1
    mn = 0
    for i in range(x - 1):
        if A[i] == 0:
            mn += 1
            if A[i + 1] == 0:
                A[i + 1] = 1
    print(mn, mx)


main()
