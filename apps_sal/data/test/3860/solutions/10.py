b = int(input())
g = int(input())
n = int(input())

max_boy = min(b, n)
min_boy = max(n - g, 0)
print(max_boy - min_boy + 1)
