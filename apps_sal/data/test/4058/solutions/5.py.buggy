import sys

n, r = list(map(int, input().split()))
A = list(map(int, input().split()))


count = 0
i = 0
while i < n:

    for j in range(min(i + r - 1, n - 1), max(i - r, -1), -1):
        if A[j] == 1:
            count += 1

            if j + r > i:
                i = j + r
                break
            else:
                print(-1)
                return

    else:
        print(-1)
        return


print(count)
