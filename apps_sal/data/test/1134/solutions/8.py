def readline():
    return list(map(int, input().split()))


def main():
    n = int(input())
    m = tuple(readline())
    md = [None] * n
    prev = 0
    for i in range(n):
        prev = md[i] = max(prev, m[i])
    prev = 0
    for i in range(n - 1, -1, -1):
        prev -= 1
        prev = md[i] = max(prev, md[i])
    print(sum(md) - sum(m))


main()
