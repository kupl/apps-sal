x, a, b = list(map(int, input().split()))

if 0 < b <= a:
    print('delicious')
elif a < b <= a + x:
    print('safe')
elif a + x < b:
    print('dangerous')
