n, a, b = map(int, input().split())

words_b = a
l_a_b = a + b

if a == 0 and b == 0:
    print('0')
    return

d, m = divmod(n, a + b)

if m == 0:
    print(words_b * d)
    return

if m <= a:
    print(int(words_b) * d + m)
else:
    print(int(words_b) * d + a)
