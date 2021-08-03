l, r = list(map(int, input().split()))
n = 0
count = 0
for pow2 in range(0, 33):
    for pow3 in range(0, 33):
        n = (2**pow2) * (3**pow3)
        if n <= r and n >= l:
            count += 1
print(count)
