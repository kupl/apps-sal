def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    tmpans1 = 0
    for i in range(N):
        tmp += A[i]
        if i % 2 == 0 and tmp <= 0:
            tmpans1 += 1 - tmp
            tmp = 1
        elif i % 2 == 1 and tmp >= 0:
            tmpans1 += 1 + tmp
            tmp = -1
    tmp = 0
    tmpans2 = 0
    for i in range(N):
        tmp += A[i]
        if i % 2 == 0 and tmp >= 0:
            tmpans2 += 1 + tmp
            tmp = -1
        elif i % 2 == 1 and tmp <= 0:
            tmpans2 += 1 - tmp
            tmp = 1
    print(min(tmpans1, tmpans2))


main()
