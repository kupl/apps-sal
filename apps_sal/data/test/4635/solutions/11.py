from string import ascii_lowercase as let


def main():
    t = int(input())
    for i in range(t):
        (n, k) = list(map(int, input().split()))
        ll = let[:k]
        s = ll * (n // len(ll))
        s += ll[:n - len(s)]
        print(s)


main()
