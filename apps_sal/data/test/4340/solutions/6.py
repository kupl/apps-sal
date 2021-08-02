n = int(input())
l = list(map(int, input().split()))
l = [x if x % 2 else x - 1 for x in l]
print(*l)
