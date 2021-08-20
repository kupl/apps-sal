n = int(input())
for _ in range(n):
    (c, s) = list(map(int, input().split()))
    a = s // c
    b = s % c
    print(b * (a + 1) ** 2 + (c - b) * a ** 2)
