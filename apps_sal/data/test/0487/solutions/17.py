def gcd(a, b):
    return gcd(b, a % b) if b else a


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    d = max(arr)
    while True:
        res = 0
        for i in arr:
            res += d - i
        if res > sum(arr):
            print(d)
            return
        d += 1


main()
