n = int(input())
a = [int(x) for x in input().split()]
mn = min(a)
mx = max(a)

print(mx - mn + 1 - n)
