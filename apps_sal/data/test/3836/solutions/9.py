import collections
import sys
import traceback


class Input(object):

    def __init__(self):
        self.fh = sys.stdin

    def next_line(self):
        while True:
            line = sys.stdin.readline()
            if line == '\n':
                continue
            return line

    def next_line_ints(self):
        line = self.next_line()
        return [int(x) for x in line.split()]

    def next_line_strs(self):
        line = self.next_line()
        return line.split()


def get_max_influence(influence):
    for i in range(4):
        influence[i].sort(reverse=True)
    t = [0] * 4
    result = 0
    while t[1] < len(influence[1]) and t[2] < len(influence[2]):
        result += influence[1][t[1]] + influence[2][t[2]]
        t[1] += 1
        t[2] += 1
    while t[3] < len(influence[3]):
        best = 0
        best_id = -1
        for i in range(3):
            if t[i] < len(influence[i]) and influence[i][t[i]] > best:
                best = influence[i][t[i]]
                best_id = i
        result += influence[3][t[3]]
        t[3] += 1
        if best_id != -1:
            result += influence[best_id][t[best_id]]
            t[best_id] += 1
    return result


def main():
    input = Input()
    while True:
        try:
            nums = input.next_line_ints()
            if not nums:
                break
            (n,) = nums
            if n == -1:
                break
            influence = [[] for _ in range(4)]
            for _ in range(n):
                (support, value) = input.next_line_strs()
                influence[int(support, 2)].append(int(value))
        except:
            print('read input failed')
        try:
            max_value = get_max_influence(influence)
            print('{}'.format(max_value))
        except:
            traceback.print_exc(file=sys.stdout)
            print('get_min_dist failed')


main()
