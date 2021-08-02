b, g, n = [int(input()) for i in range(3)]
max_man = min(n, b)
max_girl = min(n, g)
min_man = n - max_girl
print(max(0, max_man - min_man + 1))
