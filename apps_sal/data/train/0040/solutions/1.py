from sys import stdin
input = stdin.readline


def main():
    anses = []
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        f = [0] * (n + 1)
        d = sorted(list(set(a)))
        for q in range(1, len(d) + 1):
            f[d[q - 1]] = q
        for q in range(len(a)):
            a[q] = f[a[q]]
        n = len(d)
        starts, ends = [-1] * (n + 1), [n + 1] * (n + 1)
        for q in range(len(a)):
            if starts[a[q]] == -1:
                starts[a[q]] = q
            ends[a[q]] = q
        s = [0] * (n + 1)
        max1 = -float('inf')
        for q in range(1, n + 1):
            s[q] = s[q - 1] * (ends[q - 1] < starts[q]) + 1
            max1 = max(max1, s[q])
        anses.append(str(len(d) - max1))
    print('\n'.join(anses))


main()
