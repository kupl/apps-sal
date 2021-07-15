3

n = int(input())

attack = 0
dict_a = dict()
dict_b = dict()
for i in range(n):
    (x, y) = tuple(map(int, input().split()))
    (a, b) = (x+y, x-y)
    if a in dict_a:
        attack += dict_a[a]
        dict_a[a] += 1
    else:
        dict_a[a] = 1
    if b in dict_b:
        attack += dict_b[b]
        dict_b[b] += 1
    else:
        dict_b[b] = 1

print(str(attack))

