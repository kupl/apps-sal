def main():
    x1, y1, z1 = [int(s) for s in input().split()]
    x2, y2, z2 = [int(s) for s in input().split()]
    plus = min(z1, y2)
    remain = z1 - plus

    minus = max(z2 - remain - x1, 0)
    return (plus - minus) * 2


tests = int(input())
for _ in range(tests):
    print(main())
