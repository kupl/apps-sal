def solve(a, b, c):
    return (a + b + c - 1)


t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    print(solve(a, b, c))
