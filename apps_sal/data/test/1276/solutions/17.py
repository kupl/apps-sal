from collections import Counter


def main():
    n = int(input())
    s = input()
    d = Counter(s)
    a = d["R"] * d["G"] * d["B"]
    for i in range(n):
        t = min(n - i - 1, i)
        for j in range(t + 1):
            if s[i - j] != s[i] and s[i - j] != s[i + j] and s[i] != s[i + j]:
                a -= 1
    print(a)


def __starting_point():
    main()


__starting_point()
