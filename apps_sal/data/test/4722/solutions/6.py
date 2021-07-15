a, b = map(int, input().split())
print(("Impossible", "Possible")[a % 3 * b % 3 * (a + b) % 3 == 0])
