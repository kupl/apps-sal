

for _ in range(int(input())):
    h, m = map(int, input().split())

    h = 60 * h + m

    print(1440 - h)
