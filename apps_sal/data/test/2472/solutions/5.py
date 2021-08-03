def main():
    N = int(input())
    A = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(tuple([b, a]))
    A.sort()
    total = 0
    for a, b in A:
        total += b
        if a < total:
            print('No')
            return
    print('Yes')


main()
