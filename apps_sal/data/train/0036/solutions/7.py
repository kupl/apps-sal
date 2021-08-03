
# class heap:
# def __init__(self, first, last):
#self.first = first
#self.last = last
# def __contains__(self, x):
# if self.first <= x <= self.last:
# return True
# else:
# return False

def borders(nums):
    prev = 1
    for x in nums:
        yield prev, prev + x - 1
        prev += x


def inside(x, first, last):
    return first <= x <= last

#nums = list(int(x) for x in '2 7 3 4 9'.split(" "))
# print(nums)
# print(list(borders(nums)))

#j = list(int(x) for x in '1 25 11'.split(" "))


heapsamount = int(input())
nums = list(int(x) for x in input().split(" "))
jamount = int(input())
j = list(int(x) for x in input().split(" "))

#heapsamount = 5
#nums = list(int(x) for x in '2 7 3 4 9'.split(" "))
#jamount = 4
#j = [1, 25, 11, 4]

b = list(borders(nums))

# for hp, number in zip(hps, j):

#hps = list(heap(*args) for args in b)
# for number in j:
# for hp, hpnum in zip(hps, range(1,heapsamount+1)):
# if number in hp:
# print(hpnum)


sor = list([x, y, None] for x, y in zip(j, list(range(jamount))))

sor.sort(key=lambda x: x[0])

i = 0
j = 0
for number, index, n in sor:
    bord = b[i]

    while not inside(number, bord[0], bord[1]):
        i += 1
        bord = b[i]

    # while inside(number, bord[0], bord[1]):
    sor[j][2] = i + 1

    j += 1

sor.sort(key=lambda x: x[1])
for x in sor:
    print(x[2])
