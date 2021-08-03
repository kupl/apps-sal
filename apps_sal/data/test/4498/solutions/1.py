a, b, c, d = list(map(int, input().split()))
a_b = max(a, b) - min(a, b) <= d
b_c = max(b, c) - min(b, c) <= d
c_a = max(c, a) - min(c, a) <= d

if (a_b and b_c) or c_a:
    print('Yes')
else:
    print('No')
