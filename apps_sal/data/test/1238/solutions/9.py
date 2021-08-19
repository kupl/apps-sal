n = int(input())
arr = list(map(int, input().split()))
(mi, ma) = (min(arr), max(arr))
print(ma - mi + 1 - n)
