n = int(input())
print(n - (sum(map(int, input().split())) % n != 0))
