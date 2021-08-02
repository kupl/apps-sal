
def main():
    with open(0) as f:
        N = int(f.readline())
        A = list(map(int, f.readline().split()))
        B = list(map(int, f.readline().split()))

    ans = max([sum(A[:i + 1] + B[i:]) for i in range(N)])
    print(ans)


main()
