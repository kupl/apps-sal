y, m, d = list(map(int, input().split('/')))
if 10000 * y + 100 * m + d <= 20190430:
    print("Heisei")
else:
    print("TBD")
