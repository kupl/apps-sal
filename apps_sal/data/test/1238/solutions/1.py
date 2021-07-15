n = int(input())
l = list(map(int, input().split()))
mn = min(l)
mx = max(l)
print(mx - mn + 1- n)

