y, m, d = list(map(int, input().split("/")))
flg = True
if y >= 2020:
    flg = False
if y == 2019 and m >= 5:
    flg = False
print(("Heisei" if flg else "TBD"))
