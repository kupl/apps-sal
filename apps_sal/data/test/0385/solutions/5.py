class Node:
    def __init__(self, index):
        self.left = index - 1
        self.right = index + 1
        self.pair = -1

def __starting_point():
    n, m, p = map(int, input().split())
    brackets = input()
    operations = input()

    nodes = [Node(i) for i in range(n + 1)]
    stack = []

    for i in range(n):
        if brackets[i] == "(":
            stack.append(i + 1)
        else:
            pair_id = stack.pop()
            nodes[pair_id].pair = i + 1
            nodes[i + 1].pair = pair_id

    for i in range(m):
        if operations[i] == "L":
            p = nodes[p].left
        elif operations[i] == "R":
            p = nodes[p].right
        else:
            pair_id = nodes[p].pair
            
            left = min(p, pair_id)
            right = max(p, pair_id)

            left_node = nodes[left].left
            right_node = nodes[right].right

            nodes[left_node].right = right_node
            if right_node != n + 1:
                nodes[right_node].left = left_node
                p = right_node
            else:
                p = left_node

    p = nodes[0].right
    result = []
    while p != n + 1:
        result.append(brackets[p - 1])
        p = nodes[p].right

    print("".join(result))
__starting_point()
