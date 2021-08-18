from sys import stdin as fin


class node:
    def __init__(self, val=None):
        self.prev = self.next = None
        self.val = val

    @staticmethod
    def link(node1, node2):
        node1.next = node2
        node2.prev = node1
        return node2

    @staticmethod
    def move(node1, node2, inode1, inode2):
        if inode1.prev is not None:
            inode1.prev.next = inode2.next
        if inode2.next is not None:
            inode2.next.prev = inode1.prev
        node1 = node.link(node1, inode1)
        node2 = node.link(inode2, node2)
        return node1, node2


n, m, k = map(int, fin.readline().split())
arr = list(map(int, fin.readline().split()))


cur = line = node()
for num in arr:
    cur = node.link(cur, node(num))
res = 0
for i in range(n):
    buy = list(map(int, fin.readline().split()))
    for num in buy:
        cur = line
        cnt = 0
        while cur.val != num:
            cur = cur.next
            cnt += 1
        res += cnt
        if line.next != cur:
            line = node.move(line, line.next, cur, cur)[0].prev

print(res)
