def main():
    (N, A) = list(map(int, open(0).read().split()))
    if N % 500 <= A:
        print('Yes')
    else:
        print('No')


main()
