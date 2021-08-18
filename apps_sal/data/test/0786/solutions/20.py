n = int(input())


loi = []

infinity = False
impossible = False

for i in range(n):
    loi.append(list(map(int, input().split(" "))))


if loi[0][1] == 1:
    upper_bound = 99999999999999999
    lower_bound = 1900
    last_div = 1
if loi[0][1] == 2:
    upper_bound = 1899
    lower_bound = -99999999999999999
    last_div = 2


for (c, d) in loi:
    if d == 2 and lower_bound > 1899:
        impossible = True
    if d == 1 and upper_bound < 1900:
        impossible = True

    if d == 1:
        lower_bound = max(lower_bound, 1900)
    if d == 2:
        upper_bound = min(upper_bound, 1899)

    upper_bound += c
    lower_bound += c

    if lower_bound > upper_bound:
        impossible = True

    last_div = d


if impossible:
    print("Impossible")
elif upper_bound > 10000000000000000:
    print("Infinity")
else:
    print(upper_bound)
