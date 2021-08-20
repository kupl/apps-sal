n = int(input())
a = list(map(int, input().split()))
x = max(a) - min(a)
print(abs(x))
