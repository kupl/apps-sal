import math


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    right = sum(arr)
    left = 0

    arr.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        left += arr[i]
        total += i * arr[i] - left
        total += right - (n - i) * arr[i]
        right -= arr[i]

    g = math.gcd(max(total, n), min(total, n))
    total = total // g
    n = n // g

    print(total, n)


main()
