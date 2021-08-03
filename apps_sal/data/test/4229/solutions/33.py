n = int(input())
print(sum([x for x in range(1, n + 1) if x % 3 != 0 and x % 5 != 0]))
