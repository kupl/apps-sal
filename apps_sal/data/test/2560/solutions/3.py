t = int(input())
for _ in range(t):
    (n, l, r) = map(int, input().split())
    print('No' if n // l * r < n else 'Yes')
