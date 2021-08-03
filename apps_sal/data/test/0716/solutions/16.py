N, a, b = [int(x) for x in input().strip().split(" ")]
airports = input().strip()
airports = [int(x) for x in airports]

print(abs(airports[a - 1] - airports[b - 1]))
