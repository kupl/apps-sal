# python3

def solve():
    n = int(input())
    lis = list(input())
    if len(lis) % 4 != 0:
        return "==="

    counter = [0, 0, 0, 0]
    for j in lis:
        if j == "A":
            counter[0] += 1
        elif j == "C":
            counter[1] += 1
        elif j == "G":
            counter[2] += 1
        elif j == "T":
            counter[3] += 1

    avg = len(lis) / 4
    for j in range(4):
        counter[j] -= avg
        if counter[j] > 0:
            return "==="

    for j in range(len(lis)):
        if lis[j] == "?":
            if counter[0] < 0:
                lis[j] = "A"
                counter[0] += 1
            elif counter[1] < 0:
                lis[j] = "C"
                counter[1] += 1
            elif counter[2] < 0:
                lis[j] = "G"
                counter[2] += 1
            elif counter[3] < 0:
                lis[j] = "T"
                counter[3] += 1

    return "".join(lis)


print(solve())
