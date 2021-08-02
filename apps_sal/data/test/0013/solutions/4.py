def dfs(start_node, edges, colors, result):
    stack = [start_node]
    while stack:
        current_node = stack[-1]
        if colors[current_node] == 2:
            stack.pop()
            continue
        colors[current_node] = 1
        children = edges[current_node]
        if not children:
            colors[current_node] = 2
            result.append(stack.pop())
        else:
            child = children.pop()
            if colors[child] == 1:
                return False
            stack.append(child)
    return True


def find_courses_sequence(member_of_node, find_nodes, edges):
    colors = [0] * member_of_node
    result = []
    for node in find_nodes:
        if not dfs(node, edges, colors, result):
            return []
    return result


def __starting_point():
    n, k = map(int, input().split())
    main_courses = [int(c) - 1 for c in input().split()]
    courses = dict()
    for index in range(n):
        courses[index] = [int(d) - 1 for d in input().split()[1:]]

    result = find_courses_sequence(n, main_courses, courses)

    if result:
        print(len(result))
        for v in result:
            print(v + 1, end=" ")
    else:
        print(-1)


__starting_point()
