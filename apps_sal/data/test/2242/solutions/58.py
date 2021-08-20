def main():
    (n, mods) = (0, [1] + [0] * 2019)
    d = 1
    for i in reversed(input()):
        n = (n + int(i) * d) % 2019
        d = d * 10 % 2019
        mods[n] += 1
    print(sum([i * (i - 1) // 2 for i in mods]))


main()
