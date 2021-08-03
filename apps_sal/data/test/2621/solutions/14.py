import sys
input = sys.stdin.readline

testcases = int(input())
for test in range(testcases):
    n, m, k = list(map(int, input().split()))
    H = list(map(int, input().split()))

    if n == 1:
        print("YES")
        continue

    for i in range(n - 1):
        if H[i] > H[i + 1] - k:
            m += min(H[i], H[i] - (H[i + 1] - k))

        elif H[i] < H[i + 1] - k:
            m -= (H[i + 1] - k) - H[i]

        if m < 0:
            print("NO")
            break

    else:
        print("YES")
