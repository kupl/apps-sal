def main():
    n = int(input())
    A = [0 for _ in range(n)]
    B = list(map(int, input().split()))
    other = 0
    k = 0

    for i in range(n):
        b = B[i]
        d = b - other
        k += abs(d)
        other += d

    return k


print(main())
