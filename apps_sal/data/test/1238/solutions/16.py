n = int(input())
l = list(map(int, input().strip().split()))
m = max(l)
n1 = min(l)
f = (m - n1) + 1
print(f - n)
