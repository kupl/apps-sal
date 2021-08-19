(n, w) = list(map(int, input().split(' ')))
cups = list(map(int, input().split(' ')))
cups.sort()
max_girl = cups[0]
max_boy = cups[n]
x = min(max_girl, max_boy / 2.0, w / (3.0 * n))
print(3 * x * n)
