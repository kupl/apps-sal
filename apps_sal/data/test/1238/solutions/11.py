n = input()
a = list(map(int, input().split()))
x1 = min(a)
x2 = max(a)
l = x2 - x1 + 1
print(l - len(a))
