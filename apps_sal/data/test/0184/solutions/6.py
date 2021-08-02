l, r, a = list(map(int, input().split(' ')))

for i in range(a):
    if r < l:
        r += 1
    else:
        l += 1

print(2 * min(l, r))
