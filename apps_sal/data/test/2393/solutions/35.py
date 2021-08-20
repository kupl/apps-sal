t = int(input())
for i in range(t):
    s = input()
    one = set()
    two = set()
    cnt = 0
    ans = []
    for i in range(len(s) - 2):
        if s[i:i + 3] == 'one':
            one.add(i + 1)
        elif s[i:i + 3] == 'two':
            two.add(i + 1)
    both = set()
    for i in one:
        if i - 2 in two:
            both.add(i)
    print(len(one) + len(two) - len(both))
    for i in both:
        print(i, end=' ')
    for i in one:
        if not i in both:
            print(i + 1, end=' ')
    for i in two:
        if not i + 2 in both:
            print(i + 1, end=' ')
    print()
