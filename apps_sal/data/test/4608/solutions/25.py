# B - Trained?
def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    cnt = 0
    x = 1

    if 2 in a:
        for _ in range(n - 1):
            x = a[x - 1]
            cnt += 1

            if x == 2:
                print(cnt)
                return
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
