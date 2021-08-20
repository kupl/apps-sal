import sys
3


def findBiggerInInterval(list, pos, operations):
    list_slice = nbr_list[pos + 1:pos + operations + 1]
    m = max(list_slice)
    if m > list[pos]:
        for it_pos in range(pos + 1, pos + operations + 1):
            if list[it_pos] == m:
                bigger_pos = it_pos
                break
        if bigger_pos != None:
            return bigger_pos
        else:
            return -1
    return -1


def swapInPlace(list, firstPos, secondPos):
    for pos in range(secondPos, firstPos, -1):
        tmp = list[pos]
        list[pos] = list[pos - 1]
        list[pos - 1] = tmp


(number, operations) = [nbr for nbr in sys.stdin.readline().split()]
operations = int(operations)
nbr_list = list(number)
if operations > 0:
    for pos in range(len(nbr_list) - 1):
        biggerPos = findBiggerInInterval(nbr_list, pos, operations)
        if biggerPos != -1:
            swapInPlace(nbr_list, pos, biggerPos)
            operations -= biggerPos - pos
        if operations == 0:
            break
print(''.join(nbr_list))
