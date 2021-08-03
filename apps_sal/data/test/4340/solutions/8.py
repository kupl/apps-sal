n = int(input())
print(*[int(x) if int(x) % 2 else int(x) - 1 for x in input().split()])
