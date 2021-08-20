for t in range(int(input())):
    (a, b, q) = list(map(int, input().split()))
    c = a * b
    x = [0] * (c + 1)
    for i in range(c):
        if i % a % b != i % b % a:
            x[i] = 1
        x[i] += x[i - 1]

    def get(y):
        if y < 0:
            return 0
        cnt = y // c * x[c - 1]
        return cnt + x[y % c]
    ans = []
    for _ in range(q):
        (l, r) = list(map(int, input().split()))
        ans.append(get(r) - get(l - 1))
    print(*ans)
