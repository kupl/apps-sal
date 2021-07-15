#!/usr/bin/env pypy3
import sys


class BitTreeNode(object):
    __slots__ = ["left", "right", "count"]
    def __init__(self, cnt):
        self.left = None
        self.right = None
        self.count = cnt

class BitTree(object):
    
    def __init__(self):
        self.root = BitTreeNode(0)
        self.add(reversed(get_bits(0)))

    def add(self, bits):
        node = self.root
        node.count += 1
        for bit in bits:
            if bit:
                if not node.right:
                    node.right = BitTreeNode(1)
                else:
                    node.right.count += 1
                node = node.right
            else:
                if not node.left:
                    node.left = BitTreeNode(1)
                else:
                    node.left.count += 1
                node = node.left

    def remove(self, bits):
        node = self.root
        node.count -= 1
        for bit in bits:
            if bit == 0:
                node.left.count -= 1
                if node.left.count == 0:
                    node.left = None
                    return
                node = node.left
            else:
                node.right.count -= 1
                if node.right.count == 0:
                    node.right = None
                    return
                node = node.right
             
    def examine_xor(self, bits):
        best = 0
        node = self.root
        for i, bit in reversed(list(enumerate(bits))):
            assert node.count > 0
            if bit == 0:
                if node.right is not None:
                    best += 1 << i
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left is not None:
                    best += 1 << i
                    node = node.left
                else:
                    node = node.right
        return best

    @classmethod
    def print_tree(cls, node, indent):
        print(" " * indent + "+", node.count)
        if node.right:
            cls.print_tree(node.right, indent + 2)
        if node.left:
            cls.print_tree(node.left, indent + 2)


def read_query():
    qType, number = next(sys.stdin).split()
    return qType, int(number)


def get_bits(number):
    ans = []
    for _ in range(32):
        ans.append(number % 2)
        number //= 2
    return ans


def solve_and_print(q):
    tree = BitTree()
    for _ in range(q):
        qType, number = read_query()
        #print()
        #print(qType, number)
        if qType == "+":
            tree.add(reversed(get_bits(number)))
            #tree.print_tree(tree.root, 0)
        elif qType == "-":
            tree.remove(reversed(get_bits(number)))
            #tree.print_tree(tree.root, 0)
        elif qType == "?":
            print(tree.examine_xor(get_bits(number)))


def __starting_point():
    q = int(next(sys.stdin))
    solve_and_print(q)

__starting_point()
