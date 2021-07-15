def main():
    N = int(input())
    A = list(map(int, input().split()))
    l, t, n = 0, 0, 0
    for r, a in enumerate(A):
        while a & t:
            t ^= A[l]
            l += 1
        t |= a
        n += r - l + 1
    return n

print((main()))

