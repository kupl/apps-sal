def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(1)
        while len(a) > 1 and a[-1] == a[-2]:
            a.pop()
            a[-1] += 1
    print(' '.join((str(i) for i in a)))


main()
