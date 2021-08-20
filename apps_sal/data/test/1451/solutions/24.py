def main():
    (n, k) = map(int, input().strip().split())
    print(sum((s.count('4') + s.count('7') <= k for s in input().strip().split())))


main()
