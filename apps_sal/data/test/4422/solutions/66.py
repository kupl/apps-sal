n, k = map(int, input().split())
s = list(input())

for i in range(1, n + 1):
    if i == k:
        print(s[i - 1].lower(), end="")
        continue
    print(s[i - 1], end="")
