import math
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inint():
    return(int(input()))


def inlst():
    return(list(map(int, input().split())))

# returns a List of Characters, which is easier to use in Python as Strings are Immutable


def instr():
    s = input()
    return(list(s[:len(s) - 1]))


def invar():
    return(list(map(int, input().split())))


def height(num):
    return int(math.log2(num))


n, m = invar()
elems = 2**n
tree = [0] * (2 * (elems))

li = inlst()
for i in range(elems):
    tree[i + elems] = li[i]


def update_value(i):
    if (height(elems) - height(i)) % 2 == 1:
        tree[i] = tree[2 * i] | tree[2 * i + 1]
    else:
        tree[i] = tree[2 * i] ^ tree[2 * i + 1]


for i in range(elems - 1, 0, -1):
    update_value(i)


def modify(pos, val):
    pos += elems
    tree[pos] = val

    while pos > 1:
        pos >>= 1
        update_value(pos)


for _ in range(m):
    p, b = invar()
    modify(p - 1, b)
    print(tree[1])
