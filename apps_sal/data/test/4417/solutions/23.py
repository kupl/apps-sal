for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    li = list(map(int, input().split()))
    if max(li) - min(li) > 2 * k:
        print(-1)
        continue
    e = max(li)
    f = min(li)
    print(f + k)
