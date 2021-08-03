# C - Big Array
def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()

    i = 0

    while k > 0:
        k -= ab[i][1]
        i += 1
    else:
        print(ab[i - 1][0])


if __name__ == "__main__":
    main()
