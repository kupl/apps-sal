class Node:

    def __init__(self, value):
        self.parent = None
        self.val = value
        self.zero = None
        self.one = None
        self.marker = 0
        self.max_len = 0


root = Node(-1)


def add(n):
    curr_node = root
    bitstr = bin(n)[2:].zfill(32)
    for bit in bitstr:
        if bit == '1':
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


def remove(n):
    curr_node = root
    bitstr = bin(n)[2:].zfill(32)
    for bit in bitstr:
        if bit == '1':
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


def query(n):
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
            result.append('1')
        elif looking_for == 1 and one_present:
            curr_node = curr_node.one
            result.append('1')
        elif looking_for == 0 and one_present:
            curr_node = curr_node.one
            result.append('0')
        else:
            curr_node = curr_node.zero
            result.append('0')
    print(int(''.join(result), 2))


num_q = int(input())
for _ in range(num_q):
    expr = input()
    symbol = expr[0]
    num = int(expr[2:])
    add(0)
    if symbol == '+':
        add(num)
    elif symbol == '-':
        remove(num)
    elif symbol == '?':
        query(num)
