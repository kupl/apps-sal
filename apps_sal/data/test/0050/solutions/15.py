n, m, r = list(map(int, input().split()))
a = min(list(map(int, input().split())))
b = max(list(map(int, input().split())))
print(max(r, (r // a) * (b - a) + r))
