n, h = list(map(int, input().split()))

arr = list(map(int, input().split()))

print(sum(1 if h >= x else 2 for x in arr))
