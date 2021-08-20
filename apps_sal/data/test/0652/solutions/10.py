from collections import Counter


def main():
    n = int(input())
    x = []
    y = []
    a = Counter()
    for i in range(n):
        x.append(0)
        y.append(0)
        (x[i], y[i]) = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            a[x[i] + x[j], y[i] + y[j]] += 1
    ans = 0
    for (q, p) in list(a.items()):
        ans += p * (p - 1)
    ans //= 2
    print(ans)


main()
