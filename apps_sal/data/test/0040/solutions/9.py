n = int(input())

rates = []

for i in range(n):
    before, after = list(map(int, input().split()))
    rates.append(before)
    if before != after:
        print('rated')
        return

print('maybe' if rates == list(reversed(sorted(rates))) else 'unrated')
