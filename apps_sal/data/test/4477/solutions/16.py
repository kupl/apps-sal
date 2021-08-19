t = int(input())
for i in range(t):
    n = input()
    z = len(n)
    k = int(n) % 10
    print(round((k - 1) * 10 + z * (z + 1) / 2))
