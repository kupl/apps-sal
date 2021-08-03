n, k = map(int, input().split())
t = list(map(int, input().split())) + [10001]

i = 0
while t[i] < 0 and i < k:
    t[i] = - t[i]
    i += 1
if i < k:
    print(sum(t[:-1]) - 2 * ((k - i) % 2) * min(t[i], t[i - 1]))
else:
    print(sum(t[:-1]))
