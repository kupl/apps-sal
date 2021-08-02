n, a, b = list(map(int, input().split()))
coins = list(map(int, input().split()))
result = [str((x * a % b) // a) for x in coins]
print(" ".join(list(result)))
