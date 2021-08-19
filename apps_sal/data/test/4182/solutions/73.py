(n, m, x, y) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
left = max(a)
right = min(b)
if left < right and (x <= left < y or x < right <= y):
    print('No War')
else:
    print('War')
