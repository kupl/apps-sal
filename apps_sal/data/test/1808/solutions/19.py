a, b, c = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]
print(sum(tasks[:len(tasks) - b]) + b * c)
