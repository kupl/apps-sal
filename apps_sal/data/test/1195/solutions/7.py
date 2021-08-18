n = int(input())
a = list(map(int, input().split()))

min_ = min(a)

print(2 + (a[2] ^ min_))
