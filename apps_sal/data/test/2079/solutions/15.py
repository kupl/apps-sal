"""Problem B - Bus of Characters.

http://codeforces.com/contest/982/problem/B

In the Bus of Characters there are `n` rows of seat, each having `2` seats.
The width of both seats in the `i`-th row is `w_i` centimeters. All integers
`w_i` are distinct.

Initially the bus is empty. On each of `2n` stops one passenger enters the
bus. There are two types of passengers:

- an introvert always chooses a row where both seats are empty. Among these
rows he chooses the one with the smallest seats width and takes one of the
seats in it;

- an extrovert always chooses a row where exactly one seat is occupied (by an
introvert). Among these rows he chooses the one with the largest seats width
and takes the vacant place in it.

You are given the seats width in each row and the order the passengers enter
the bus. Determine which row each passenger will take.

Input:

The first line contains a single integer `n` (`1 <= n <= 200\,000`) — the
number of rows in the bus.

The second line contains the sequence of integers `w_1, w_2, ..., w_n` (`1 <=
w_i <= 10^{9}`), where `w_i` is the width of each of the seats in the `i`-th
row. It is guaranteed that all `w_i` are distinct.

The third line contains a string of length `2n`, consisting of digits '0' and
'1' — the description of the order the passengers enter the bus. If the `j`-th
character is '0', then the passenger that enters the bus on the `j`-th stop is
an introvert. If the `j`-th character is '1', the the passenger that enters the
bus on the `j`-th stop is an extrovert. It is guaranteed that the number of
extroverts equals the number of introverts (i. e. both numbers equal `n`), and
for each extrovert there always is a suitable row.

Output:

Print `2n` integers — the rows the passengers will take. The order of
passengers should be the same as in input.

"""
import logging
import collections


fmt = '%(levelname)s - %(name)s (line:%(lineno)s) - %(message)s'
formatter = logging.Formatter(fmt)

ch = logging.StreamHandler()
ch.setLevel(logging.NOTSET)
ch.setFormatter(formatter)

logger = logging.getLogger('bus_of_characters')
logger.setLevel(logging.NOTSET)
logger.addHandler(ch)


def solve(w, s):
    free = collections.deque()
    used = collections.deque()

    for w in sorted(enumerate(w), key=lambda x: x[1]):
        free.append([w[0] + 1, w[1]])
    
    ids = [-1] * len(s)

    order = []
    for pid, p in enumerate(s):
        logger.debug('pid: %s', pid)
        if p == '0':
            taken = free.popleft(), 
            used.appendleft(taken)
            # order.append(pid, taken[0])
        else:
            logger.debug('used %s', used)
            taken = used.popleft()
        #order.append([pid, taken[0]])
        ids[pid] = taken[0]

    return [x for x, y in ids]



def main():
    n = int(input().strip())
    w = [int(x) for x in input().strip().split()]
    s = input().strip()

    result = solve(w, s)
    print(' '.join(map(str, result)))


def __starting_point():
    main()

__starting_point()
