"""
    http://codeforces.com/problemset/problem/698/A

"""
from sys import stdin, stdout
from array import array


def solve(days):
    rest_num = 0
    prev_act = 0
    for i in range(0, len(days)-1):
        cur_act = days[i]
        next_act = days[i+1]
        # stdout.write(str(cur_act))
        if cur_act == 0 or prev_act == cur_act:
            prev_act = 0
            rest_num += 1
        elif prev_act != cur_act and cur_act != 3:
            prev_act = cur_act
        else:  # cur_act == 3
            if prev_act in (1, 2):
                prev_act = prev_act % 2 + 1
            else:
                if next_act in (1, 2):
                    prev_act = next_act % 2 + 1

        # rest_num += 1
    return rest_num


def __starting_point():
    use_stdio = True
    days = []
    if use_stdio:
        length = int(stdin.readline())
        days = array('i', list(map(int, stdin.readline().split()))+[3])
        stdout.write(str(solve(days)))
    else:
        with open('input', 'r') as fin, open('output', 'w') as fout:
            length = int(fin.readline())
            days = array('i', list(map(int, fin.readline().split()))+[3])
            fout.write(str(solve(days)))

__starting_point()
