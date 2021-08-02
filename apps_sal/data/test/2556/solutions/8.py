t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    rem = b % a
    div = b // a
    print(b % a * (1 + div)**2 + (a - b % a) * (div)**2)
