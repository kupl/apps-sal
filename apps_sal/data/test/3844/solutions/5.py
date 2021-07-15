_ = input()

aa = list(map(int, input().split()))

dd = {}

for a in aa:
    if a not in dd:
        dd[a] = 1
    else:
        dd[a] += 1

odd_found = False

for k in list(dd.keys()):
    if dd[k] % 2 == 1:
        odd_found = True

if odd_found:
    print("Conan")
else:
    print("Agasa")

