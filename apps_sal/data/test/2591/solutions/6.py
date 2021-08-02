def main():
    t = int(input())
    for tt in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        l.sort()
        t = []
        if n % 2:
            t.append(l[n // 2])
        for i in range(n // 2):
            t.append(l[n // 2 - i - 1])
            t.append(l[(n + 1) // 2 + i])
        print(*t)


main()
