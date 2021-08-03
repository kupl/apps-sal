a, b, k = map(int, input().split())
cou = 0
for i in range(100):
    if a % (100 - i) == b % (100 - i) == 0:
        cou += 1
        if cou == k:
            print(100 - i)
            return
