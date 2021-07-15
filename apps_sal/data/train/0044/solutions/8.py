def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = []
        for i in range(n):
            p.append(4 * n - i * 2)
        print(*p)
main()
