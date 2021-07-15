n = int(input())
t, a = list(map(int, input().split()))
b = [abs(a - (t - i * 0.006)) for i in list(map(int, input().split()))]
print((b.index(min(b)) + 1))

