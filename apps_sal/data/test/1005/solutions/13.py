t = int(input())
for _ in range(t):
    (n, k, d) = list(map(int, input().split()))
    answer = d
    films = tuple((int(v) for v in input().split()))
    for l in range(n - d + 1):
        s = len(set(films[l:l + d]))
        if answer > s:
            answer = s
        if answer == 1:
            break
    print(answer)
