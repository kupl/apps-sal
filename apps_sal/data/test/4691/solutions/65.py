N = int(input())
dic = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for i in range(N):
    S = input()
    if S == "AC":
        dic["AC"] += 1
    elif S == "WA":
        dic["WA"] += 1
    elif S == "TLE":
        dic["TLE"] += 1
    else:
        dic["RE"] += 1

for key in list(dic.keys()):
    print(("{0} x {1}".format(key, dic[key])))
