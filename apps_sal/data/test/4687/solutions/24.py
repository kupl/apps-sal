(n, k) = [int(i) for i in input().split()]


class Number:

    def __init__(self, number, times):
        self.number = number
        self.times = times

    def __eq__(self, other):
        if self.number == other.number:
            return True
        return False

    def __le__(self, other):
        if self.number <= other.number:
            return True
        return False

    def __lt__(self, other):
        if self.number < other.number:
            return True
        return False

    def __ge__(self, other):
        if self.number >= other.number:
            return True
        return False

    def __gt__(self, other):
        if self.number > other.number:
            return True
        return False


number_list = []
for i in range(n):
    (number, times) = [int(i) for i in input().split()]
    number_list.append(Number(number, times))
number_list.sort()


def get(number_list, k):
    i = 0
    while True:
        taishou = number_list[i]
        k = k - taishou.times
        if k <= 0:
            return taishou.number
        else:
            i += 1


print(get(number_list, k))
