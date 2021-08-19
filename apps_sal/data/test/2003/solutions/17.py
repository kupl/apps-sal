# TRIE

class Node:
    def __init__(self, value):
        self.parent = None
        self.val = value
        self.zero = None
        self.one = None
        self.marker = 0
        self.max_len = 0


root = Node(-1)


def insertnode(n):
    # print("Add", n)

    curr_node = root
    bitstr = bin(n)[2:].zfill(32)  # 32-bit string

    for bit in bitstr:
        if bit == "1":
            if curr_node.one == None:
                curr_node.one = Node(1)
                curr_node.one.parent = curr_node
            curr_node = curr_node.one
        else:
            if curr_node.zero == None:
                curr_node.zero = Node(0)
                curr_node.zero.parent = curr_node
            curr_node = curr_node.zero

    curr_node.marker += 1


def delete(n):
    # print("Remove", n)

    curr_node = root
    bitstr = bin(n)[2:].zfill(32)
    for bit in bitstr:
        if bit == "1":
            curr_node = curr_node.one
        else:
            curr_node = curr_node.zero

    curr_node.marker -= 1
    if curr_node.marker == 0:
        while curr_node.parent != None:
            if curr_node.one is None and curr_node.zero is None:
                if curr_node.val == 1:
                    curr_node.parent.one = None
                else:
                    curr_node.parent.zero = None
            curr_node = curr_node.parent


def find(n):
    # print("Query", n)

    bitstr = bin(n)[2:].zfill(32)
    curr_node = root
    result = []

    for bit in bitstr:

        b = int(bit)
        looking_for = 1 - b

        zero_present = curr_node.zero != None
        one_present = curr_node.one != None

        if looking_for == 0 and zero_present:
            curr_node = curr_node.zero
            result.append("1")

        elif looking_for == 1 and one_present:
            curr_node = curr_node.one
            result.append("1")

        elif looking_for == 0 and one_present:
            curr_node = curr_node.one
            result.append("0")
        else:
            curr_node = curr_node.zero
            result.append("0")

    return int("".join(result), 2)


insertnode(0)

y = int(input())

for j in range(y):
    b = list(map(str, input().split()))
    if b[0] == "+":
        insertnode(int(b[1]))

    elif b[0] == "-":
        delete(int(b[1]))

    else:
        print(find(int(b[1])))
