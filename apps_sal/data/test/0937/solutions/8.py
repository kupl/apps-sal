from collections import Counter

def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(solve(n, k, a, t))

def solve(n, k, a, t):
    minsum = sum(ai for ai, ti in zip(a,t) if ti == 1)
    inc = sum(ai for ai, ti in zip(a[:k], t[:k]) if ti == 0)
    best_inc = inc
    for i in range(1, n - k + 1):
        if t[i - 1] == 0:
            inc -= a[i - 1]
        if t[i + k - 1] == 0:
            inc += a[i + k - 1]
        if inc > best_inc:
            best_inc = inc
    return minsum + best_inc

main()

