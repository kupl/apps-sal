m = int(input())
for q in range(m):
    n, x, y, d = list(map(int, input().split()))
    answer = float('inf')
    if y % d == 1:
        answer = (x - 2) // d + 1 + (y - 1) // d
    if y % d == n % d:
        answer = min(answer, (n - x - 1) // d + 1 + (n - y) // d)
    if y % d == x % d:
        answer = min(answer, abs(x - y) // d)
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
