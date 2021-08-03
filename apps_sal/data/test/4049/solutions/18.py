n = int(input())

a1, a2, a3 = list(map(int, input().split()))
b1, b2, b3 = list(map(int, input().split()))

min_wins = n - (min(a1, n - b2) + min(a2, n - b3) + min(a3, n - b1))
max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)

print(min_wins, max_wins)
