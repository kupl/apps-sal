gcd = lambda a, b: gcd(b, a % b) if b else a


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        total = 0
        total -= b * (c // 2)
        total += a * (c // 2)
        if c % 2:
            total += a
        print(total)




main()
