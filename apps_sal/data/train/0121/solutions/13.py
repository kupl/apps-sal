def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort()
        print(a[n] - a[n - 1])


main()
