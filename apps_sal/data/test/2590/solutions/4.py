for tc in range(int(input())):
    (n, w) = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    ls.sort(reverse=True)
    sm = 0
    i = 0
    while i != n:
        sm += ls[i]
        if sm < w * (i + 1):
            break
        i += 1
    print(i)
