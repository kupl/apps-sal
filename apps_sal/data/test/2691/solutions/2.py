def findLen(A, n, k, ch):
    maxlen = 1
    cnt = 0
    l = 0
    r = 0

    while r < n:

        if A[r] != ch:
            cnt += 1

        while cnt > k:
            if A[l] != ch:
                cnt -= 1
            l += 1

        maxlen = max(maxlen, r - l + 1)
        r += 1

    return maxlen


def answer(A, n, k):
    maxlen = 1
    for i in range(26):
        maxlen = max(maxlen, findLen(A, n, k,
                                     chr(i + ord('A'))))
        maxlen = max(maxlen, findLen(A, n, k,
                                     chr(i + ord('a'))))

    return maxlen


n, k = map(int, input().split())
s = str(input())
print(answer(s, n, k))
