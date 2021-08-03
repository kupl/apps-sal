N = int(input())
S = list(map(int, input().split()))


def findout(n):
    cnt = 0
    while n % 2 == 0:
        n = n // 2
        cnt += 1

    return cnt


A = [findout(s) for s in S]
print((sum(A)))
