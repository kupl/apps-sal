def solve(n, k, s):
    nextone = [-1] * n
    last = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            last = i
        nextone[i] = last
    prev = float('-inf')
    sol = 0
    for i in range(n):
        if s[i] == '1':
            prev = i
        else:
            if i - prev > k and nextone[i] - i > k:
                sol += 1
                prev = i
    return sol


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
