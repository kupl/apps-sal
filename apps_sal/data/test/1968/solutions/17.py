(n, v) = map(int, input().split())
wins = set()
for i in range(n):
    s = list(map(int, input().split()))
    k = s[0]
    for j in range(1, k + 1):
        if s[j] < v:
            wins.add(i + 1)
            break
print(len(wins))
print(' '.join(map(str, sorted(wins))))
