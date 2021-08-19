(n, k, p, x, y) = [int(token) for token in input().split()]
l = [int(token) for token in input().split()]
k_lower = sum((1 for a in l if a < y))
k_upper = k - k_lower
ik_lower = int((n - 1) / 2) - k_lower
ik_upper = int((n + 1) / 2) - k_upper
if ik_lower < 0:
    print('-1')
elif ik_upper < 0:
    if ik_lower + ik_upper + sum(l) > x:
        print('-1')
    else:
        l = [1] * (ik_lower + ik_upper)
        l_string = (str(a) for a in l)
        print(' '.join(l_string))
elif ik_lower + y * ik_upper + sum(l) > x:
    print('-1')
else:
    il_lower = [1] * ik_lower
    il_upper = [y] * ik_upper
    l = il_lower + il_upper
    l_string = (str(a) for a in l)
    print(' '.join(l_string))
