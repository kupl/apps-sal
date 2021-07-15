def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                print(j + 1, j + 2)
                a[j], a[j + 1] = a[j + 1], a[j]



def __starting_point():
    main()

__starting_point()
