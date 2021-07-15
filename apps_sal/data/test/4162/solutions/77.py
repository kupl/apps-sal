def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)-N
    print(ans)

def __starting_point():
    main()

__starting_point()
