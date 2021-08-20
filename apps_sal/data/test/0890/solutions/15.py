def generate(i, real, a):
    if i == n:
        if real >= 2:
            min_a = a[0]
            max_a = a[real - 1]
            sum_a = sum(a)
            if sum_a >= l and sum_a <= r and (max_a - min_a >= x):
                count[0] += 1
    else:
        generate(i + 1, real + 1, a + [c[i]])
        generate(i + 1, real, a)


(n, l, r, x) = map(int, input().split())
c = sorted(list(map(int, input().split())))
count = [0]
generate(0, 0, [])
print(count[0])
