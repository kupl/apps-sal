

def borders(nums):
    prev = 1
    for x in nums:
        yield prev, prev + x - 1
        prev += x


def inside(x, first, last):
    return first <= x <= last


heapsamount = int(input())
nums = list(int(x) for x in input().split(" "))
jamount = int(input())
j = list(int(x) for x in input().split(" "))


b = list(borders(nums))


sor = list([x, y, None] for x, y in zip(j, list(range(jamount))))

sor.sort(key=lambda x: x[0])

i = 0
j = 0
for number, index, n in sor:
    bord = b[i]

    while not inside(number, bord[0], bord[1]):
        i += 1
        bord = b[i]

    sor[j][2] = i + 1

    j += 1

sor.sort(key=lambda x: x[1])
for x in sor:
    print(x[2])
