def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    count = 0
    for j in range(n, 0, -1):
        for i in range(2**j-2, 2**(j+1)-2, 2):
            d = max(a[i] , a[i+1])- min(a[i], a[i+1])
            count += d
            if i:
                a[i//2-1] += max(a[i] , a[i+1])
    print(count)
def __starting_point():
    main()

__starting_point()
