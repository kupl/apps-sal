import sys


def main():
    for _ in range(int(input())):
        n, k = get_ints()
        s = list(input())
        x = []
        for i in range(n):
            if s[i] == "0":
                x.append((i, i - len(x)))
        i = 0
        while k > 0 and i < len(x):
            if x[i][1] < k:
                s[i], s[x[i][0]] = s[x[i][0]], s[i]
                k -= x[i][1]
                i += 1
            else:
                s[x[i][0] - k], s[x[i][0]] = s[x[i][0]], s[x[i][0] - k]
                break
        print(*s, sep="")


input = lambda: sys.stdin.readline().strip()
get_ints = lambda: map(int, input().split())
get_array = lambda: list(map(int, input().split()))
main()

