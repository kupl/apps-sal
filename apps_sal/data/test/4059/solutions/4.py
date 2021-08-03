def main():
    n = int(input())
    m = int(n**0.5) + 1
    ans = 0
    for a in range(1, m):
        for b in range(a, n):
            if a * b < n:
                if a != b:
                    ans += 2
                else:
                    ans += 1
            else:
                break
    print(ans)


main()
