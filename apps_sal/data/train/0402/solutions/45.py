def get_children(point, target):
    children = []
    (y, x) = point
    (size_y, size_x) = target
    if y - 1 >= 0:
        children.append((y - 1, x))
    if x - 1 >= 0:
        children.append((y, x - 1))
    if y + 1 <= size_y:
        children.append((y + 1, x))
    if x + 1 <= size_x:
        children.append((y, x + 1))
    return children


def bfs(source, target, is_blocked):
    queue = []
    marked = set()
    queue.append((source, 1))
    marked.add(source)
    while queue:
        (node_id, depth) = queue.pop(0)
        if depth > 200:
            return True
        for child_id in get_children(node_id, (1000000, 1000000)):
            if child_id in is_blocked:
                continue
            if child_id == target:
                return True
            if child_id not in marked:
                queue.append((child_id, depth + 1))
                marked.add(child_id)
    return False


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        is_blocked = set()
        for item in blocked:
            is_blocked.add(tuple(item))
        target = tuple(target)
        source = tuple(source)
        if bfs(source, target, is_blocked) and bfs(target, source, is_blocked):
            return True
        return False
