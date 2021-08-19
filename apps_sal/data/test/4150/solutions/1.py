n, k = map(int, input().split())

lst = map(int, input().split())


def debug():

    print('-')
    lst = [0 for _ in range(n)]
    for i in range(n):
        node = table[i]
        lst[node.index] = node.team

    print(''.join(str(x) for x in lst))
    print('-')


class Node:

    def __init__(self, index):
        self.index = index
        self.team = 0
        self.prev = None
        self.next = None


table = [None for _ in range(n)]

prev_node = None
for index, element in enumerate(lst):

    node = Node(index)

    if prev_node:
        prev_node.next = node

    node.prev = prev_node

    table[element - 1] = node
    prev_node = node

team = 1
for i in reversed(range(n)):

    # taken
    if table[i].team != 0:
        continue

    node = table[i]
    node.team = team

    next_node = node.next
    for j in range(k):

        if next_node is None:
            break

        next_node.team = team
        next_node = next_node.next

    prev_node = node.prev
    for j in range(k):

        if prev_node is None:
            break

        prev_node.team = team
        prev_node = prev_node.prev

    if prev_node is not None:
        prev_node.next = next_node

    if next_node is not None:
        next_node.prev = prev_node

    team = 1 if team == 2 else 2

lst = [0 for _ in range(n)]
for i in range(n):
    node = table[i]
    lst[node.index] = node.team

print(''.join(str(x) for x in lst))
