from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    r = []
    l = []
    for i in range(N):
        r += (i - A[i],)
        l += (i + A[i],)
    c = Counter(l)
    for i in r:
        count += c[i]
    print(count)


main()
