
n = int(input().strip())
ais = list(map(int, input().strip().split()))

if n < 2 or (n == 2 and ais[0] == ais[1]):
    print(-1)
else:
    print(1)
    print(ais.index(min(ais)) + 1)
