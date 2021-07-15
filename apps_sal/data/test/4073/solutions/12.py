n = int(input())
a = [int(x) for x in input().split()]

k = max(a)
print(k ^ a[-1])
