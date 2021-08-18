j, s, m = map(int, input().split())
m = m - j
buy = m // s
if(buy % 2 == 0):
    print("Lucky Chef")
else:
    print("Unlucky Chef")
