
def __starting_point():

    n = int(input())
    s = list(input())

    R = s.count("R")
    G = s.count("G")
    B = s.count("B")

    sm = R * G * B

    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                    sm -= 1
    print(sm)


__starting_point()
