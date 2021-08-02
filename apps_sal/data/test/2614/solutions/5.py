for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * n
    for e in arr:
        freq[e - 1] += 1
    m = max(freq)
    c = freq.count(m)
    print((n - (m * c)) // (m - 1) + c - 1)
