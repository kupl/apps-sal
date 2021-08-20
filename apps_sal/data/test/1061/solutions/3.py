for i in range(5):
    t = input().split()
    if '1' in t:
        print(abs(i - 2) + abs(t.index('1') - 2))
