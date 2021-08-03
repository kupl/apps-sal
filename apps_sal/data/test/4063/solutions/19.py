N = int(input())
d = list(map(int, input().split()))

d = sorted(d)
mid = N // 2
s = d[mid - 1]
f = d[mid]
print(f - s)
