def solve(n, a):
    d = {}
    for i, aa in enumerate(a):
        if aa in d:
            d[aa].append(i)
        else:
            d[aa] = [i]
    for k in d:
        if len(d[k]) > 2:
            return "YES"
        if len(d[k]) == 2:
            if d[k][1] - d[k][0] > 1:
                return "YES"
    return "NO"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(n, a))


main()

