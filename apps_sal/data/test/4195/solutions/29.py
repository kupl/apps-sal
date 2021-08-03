d, n = list(map(int, input().split()))
start = 100 ** d
counter = 0
while True:
    if start % (100 ** d) == 0 and start % (100 ** (d + 1)) != 0:
        counter += 1
    if counter == n:
        print(start)
        break
    start += 100 ** d
