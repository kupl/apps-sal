from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    s = sum(a)
    q = int(input())
    for i in range(q):
        b, c = map(int, input().split())
        s -= b * d[b]
        s += c * d[b]
        print(s)
        d[c] += d[b]
        d[b] = 0


main()
