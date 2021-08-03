n = int(input())
sp = list(map(int, input().split()))
pr = 0
posl = ""
l = 0
r = n - 1
while True:
    fl = True
    if sp[l] < sp[r]:
        if sp[l] > pr:
            pr = sp[l]
            l += 1
            posl += "L"
        elif sp[r] > pr:
            pr = sp[r]
            r -= 1
            posl += "R"
        else:
            fl = False
    else:
        if sp[r] > pr:
            pr = sp[r]
            r -= 1
            posl += "R"
        elif sp[l] > pr:
            pr = sp[l]
            l += 1
            posl += "L"
        else:
            fl = False
    if not fl:
        break
print(len(posl))
print(posl)
