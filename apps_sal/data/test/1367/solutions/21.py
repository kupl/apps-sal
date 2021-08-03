n = int(input())
series = set(map(int, input().split()))

print(*(set(range(1, n + 1)) - series))
