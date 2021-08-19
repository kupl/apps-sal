n = int(input())
s = list(map(int, input().split()))
for i in range(n):
    for j in range(n - i - 1):
        if s[j] > s[j + 1]:
            print(j + 1, j + 2)
            (s[j], s[j + 1]) = (s[j + 1], s[j])
