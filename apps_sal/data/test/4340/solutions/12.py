n = int(input())
ans = [int(x) - (int(x) + 1) % 2 for x in input().split()]
print(*ans)
