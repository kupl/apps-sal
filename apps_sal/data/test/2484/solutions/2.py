def main():
    N = int(input())
    A = list(map(int, input().split()))

    l, r = 1, 0
    t = A[0]
    n = 1
    while l < N:
        if A[l] & t:
            t ^= A[r]
            r += 1
            continue
        t |= A[l]
        l += 1
        n += l - r
    return n


print((main()))
