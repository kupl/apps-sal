n = int(input())
(x, y) = map(int, input().split())
dis1 = abs(x - 1 - y + 1) + min(x - 1, y - 1)
dis2 = abs(n - x - n + y) + min(n - x, n - y)
print(('White', 'Black')[dis1 > dis2])
