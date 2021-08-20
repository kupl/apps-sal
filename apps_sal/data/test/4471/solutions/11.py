def solve(n, a):
    mn = min(a)
    a = [i - mn for i in a]
    for i in a:
        if i % 2:
            return 'NO'
    return 'YES'


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(n, a))


main()
