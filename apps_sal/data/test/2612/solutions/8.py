t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().strip().split()))

    result = [1] * len(s)
    for i in range(len(s)):
        indeks = i + 1
        start = 2*indeks
        while start <= n:
            if s[start-1] > s[i]:
                result[start-1] = max(result[start-1], result[i] + 1)
            start += indeks
    print(max(result))
