from itertools import accumulate
N = int(input())
A = tuple(map(int, input().split()))

CA = list(accumulate(A))

mindiff = CA[-1]
left = 0
right = 2
for c in range(1, N - 1):
    # left side
    p = CA[left]
    q = CA[c] - CA[left]
    while True:
        pi = CA[left + 1]
        qi = CA[c] - CA[left + 1]
        if abs(pi - qi) >= abs(p - q):
            break
        p = pi
        q = qi
        left += 1

    # right side
    r = CA[right] - CA[c]
    s = CA[-1] - CA[right]
    while True:
        ri = CA[right + 1] - CA[c]
        si = CA[-1] - CA[right + 1]
        if abs(ri - si) >= abs(r - s):
            break
        r = ri
        s = si
        right += 1

    mindiff = min(mindiff, max(p, q, r, s) - min(p, q, r, s))
print(mindiff)
