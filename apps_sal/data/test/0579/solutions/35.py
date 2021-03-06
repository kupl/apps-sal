from numba import jit


@jit
def main():
    (n, k) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        (start, count) = (i, 1)
        val = c[start]
        while p[start] - 1 != i:
            start = p[start] - 1
            count += 1
            val += c[start]
        start = i
        if val > 0:
            a = (k // count - 1) * val
            ans = max(a, ans)
            num = count + k % count
        else:
            a = 0
            num = min(k, count)
        for _ in range(num):
            start = p[start] - 1
            a += c[start]
            ans = max(a, ans)
    print(ans)


main()
