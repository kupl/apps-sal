def gcd(a, b):
    return gcd(b, a % b) if b else a


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = []
    for i in range(len(arr) - 1, 0, -1):
        arr[i] -= arr[i - 1]
    for i in range(1, len(arr) + 1):
        f = 1
        for j in range(0, i):
            for k in range(j + i, len(arr), i):
                if arr[j] != arr[k]:
                    f = 0
                    break
        if f:
            brr.append(i)
    print(len(brr))
    print(*brr)


main()
