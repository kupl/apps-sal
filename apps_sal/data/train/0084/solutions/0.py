from sys import stdin


def solve(a):
    stack = [None]
    node_stack = [[1, {}]]
    trie = node_stack[-1]
    counter = 0
    for i in range(len(a)):
        el = a[i]
        if len(stack) == 0 or stack[-1] != el:
            current_node = node_stack[-1]
            stack.append(el)
            if el not in current_node[1]:
                current_node[1][el] = [0, {}]
            next_node = current_node[1][el]
            next_node[0] += 1
            node_stack.append(next_node)
        else:
            stack.pop()
            node_stack.pop()
            node_stack[-1][0] += 1
        value = node_stack[-1][0]
        counter -= (value - 1) * (value - 2) // 2
        counter += value * (value - 1) // 2
    return counter


q = int(stdin.readline().strip())
for _ in range(q):
    n = int(stdin.readline().strip())
    a = [int(i) for i in stdin.readline().strip().split()]
    print(solve(a))
