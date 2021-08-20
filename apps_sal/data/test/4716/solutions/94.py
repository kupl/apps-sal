def main():
    (_, k) = map(int, input().split())
    l = list(map(int, input().split()))
    cnt = 0
    l.sort(reverse=True)
    for i in range(k):
        cnt += l[i]
    else:
        print(cnt)


if __name__ == '__main__':
    main()
