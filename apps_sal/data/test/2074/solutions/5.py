n, m = list(map(int, input().split()))

streets = []

for a in range(0, n):
    street = list(map(int, input().split()))
    streets.append(min(street))

print(max(streets))
