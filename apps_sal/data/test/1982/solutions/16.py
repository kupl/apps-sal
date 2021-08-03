for _ in range(int(input())):
    n, k = map(int, input().split())
    if k & 1 == n & 1 and n >= k * k:
        print("YES")
    else:
        print("NO")
