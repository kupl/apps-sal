for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n < k:
        print(k-n)
        continue
    for ans in range(2):
        a = n+ans
        if (a-k) % 2 == 0:
            print(ans)
            break

