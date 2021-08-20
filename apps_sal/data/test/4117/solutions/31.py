def isTri(a, b, c):
    if (a != b and b != c and (c != a)) and (a + b > c and b + c > a and (c + a > b)):
        return True
    else:
        return False


def main():
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if isTri(l[i], l[j], l[k]):
                    c += 1
    print(c)


main()
