def solve():
    a, b = list(map(int, input().split()))
    print((b - a % b) % b)


for i in range(int(input())):
    solve()
