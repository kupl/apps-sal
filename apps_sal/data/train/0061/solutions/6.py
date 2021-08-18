def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 2):
        if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
            print("YES")
            print(i + 1, i + 2, i + 3)
            return
    print("NO")


def test():
    t = int(input())
    while t:
        main()
        t -= 1


test()
