n = int(input())
m = list(map(int, input().split()))
print(max(m) ^ m[-1])
