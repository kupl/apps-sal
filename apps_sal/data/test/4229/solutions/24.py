N = int(input())
print(sum(map(lambda x: x if (x % 3 != 0) and (x % 5 != 0) else 0, list(range(N + 1)))))
