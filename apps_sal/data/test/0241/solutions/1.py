[n, m, min_t, max_t], t = list(map(int, input().split())), list(map(int, input().split()))
min_m, max_m = min(t), max(t)
if min_m >= min_t and max_m <= max_t and (n - m) >= ((min_m != min_t) + (max_m != max_t)):
    print('Correct')
else:
    print('Incorrect')

