ABCD = list(input())
(a, b, c, d) = (int(ABCD[0]), int(ABCD[1]), int(ABCD[2]), int(ABCD[3]))
if a + b + c + d == 7:
    print('{0}+{1}+{2}+{3}=7'.format(a, b, c, d))
elif a + b + c - d == 7:
    print('{0}+{1}+{2}-{3}=7'.format(a, b, c, d))
elif a + b - c + d == 7:
    print('{0}+{1}-{2}+{3}=7'.format(a, b, c, d))
elif a - b + c + d == 7:
    print('{0}-{1}+{2}+{3}=7'.format(a, b, c, d))
elif a - b - c + d == 7:
    print('{0}-{1}-{2}+{3}=7'.format(a, b, c, d))
elif a + b - c - d == 7:
    print('{0}+{1}-{2}-{3}=7'.format(a, b, c, d))
elif a - b + c - d == 7:
    print('{0}-{1}+{2}-{3}=7'.format(a, b, c, d))
elif a - b - c - d == 7:
    print('{0}-{1}-{2}-{3}=7'.format(a, b, c, d))
