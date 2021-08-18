

from sys import stdin

max_val = int(10e12)
min_val = int(-10e12)


def read_int(): return int(stdin.readline())
def read_ints(): return [int(x) for x in stdin.readline().split()]
def read_str(): return input()
def read_strs(): return [x for x in stdin.readline().split()]


nb_guest = read_int()
left, rite = [], []
for _ in range(nb_guest):
    a, b = read_ints()
    left.append(a)
    rite.append(b)
left = sorted(left)
rite = sorted(rite)
answ = nb_guest
for i in range(nb_guest):
    answ += max(left[i], rite[i])
print(answ)
