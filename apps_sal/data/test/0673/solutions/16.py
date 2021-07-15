def main():
    n, k = list(map(int, input().split()))
    if n % k == 0:
        print(n + k)
    else:
        print(((n // k) + 1) * k)

main()

