DEBUG = False

def print_debug(*args):
    if DEBUG:
        print(*args)


def print_res():
    nonlocal places
    nonlocal ss
    print(ss)
    for row_i in range(n):
        print("".join(places[row_i]))


n, k = [int(x) for x in input().split()]
places = []

ss = 0

for row_i in range(n):
    row = list(input())
    places.append(row)
    for i in range(12):
        if k > 0 and row[i] == "." and (i == 0 or row[i - 1] != "S") and (i == 11 or row[i + 1] != "S"):
            row[i] = "x"
            k -= 1
        if row[i] == "S":
            if i > 0 and (row[i - 1] not in [".", "-"]):
                ss += 1
            if i < 11 and (row[i + 1] not in [".", "-"]):
                ss += 1

print_debug("--------")
print_debug(k)
#print_res()

if k > 0:
    for row_i in range(n):
        if k == 0:
            break
        row = places[row_i]
        for i in range(12):
            if k == 0:
                break
            if row[i] == ".":
                if i in [1, 5, 6, 10] and row[i - 1] == "S" and row[i + 1] == "S":
                    continue
                k -= 1
                ss += 1
                row[i] = "x"

print_debug("--------")
print_debug(k)
#print_res()

if k > 0:
    for row_i in range(n):
        if k == 0:
            break
        row = places[row_i]
        for i in range(12):
            if k == 0:
                break
            if row[i] == ".":
                row[i] = "x"
                ss += 2
                k -= 1

print_debug(k)
print_res()


