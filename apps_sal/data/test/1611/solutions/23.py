n = int(input())
a = list(map(int, input().split()))
m = max(a)
s = sum(a) - m
print(m - s + 1)
