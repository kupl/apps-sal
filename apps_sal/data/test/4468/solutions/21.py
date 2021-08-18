def main():
    n, t = map(int, input().split())
    s = list(map(int, input().split()))
    cnt = n * t

    for i in range(n - 1):
        if s[i + 1] - s[i] < t:
            cnt -= s[i] + t - s[i + 1]
    else:
        print(cnt)


if __name__ == "__main__":
    main()
