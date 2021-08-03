def main():
    n = int(input())
    s = input()
    sm = s.count("R") * s.count("G") * s.count("B")
    for i in range(1, (n - 1) // 2 + 1):
        for j in range(n - 2 * i):
            if len(set(s[j] + s[j + i] + s[j + 2 * i])) == 3:
                sm -= 1
    print(sm)


main()
