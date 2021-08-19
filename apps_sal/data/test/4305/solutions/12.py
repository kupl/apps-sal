(h, a) = map(int, input().split())
if h // a == h / a:
    print(h // a)
else:
    print(h // a + 1)
