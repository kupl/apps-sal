def main():
    rdl = list(map(int, input().split()))
    (n, x) = rdl
    minutes = 0
    cur = 1
    bests = []
    for i in range(n):
        bests.append(list(map(int, input().split())))
    for i in bests:
        j = 1
        while cur + x * j <= i[0]:
            j += 1
        cur += x * (j - 1)
        minutes += i[1] - cur + 1
        cur += i[1] - cur + 1
    print(minutes)


main()
