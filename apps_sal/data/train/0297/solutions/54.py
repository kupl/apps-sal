class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) < 2:
            return len(tiles)
        nodes = []
        for letter in tiles:
            nodes.append(Node(letter))
        for node in nodes:
            for other_node in nodes:
                if node != other_node:
                    node.edges.append(other_node)
        paths = set()
        seen = set()
        for node in nodes:
            self.backtrack(node, seen, node.char, paths)
        print(paths)
        return len(paths)

    def backtrack(self, node, seen: set, path: str, paths: set):
        if node in seen:
            return
        path += node.char
        if path and path not in paths:
            paths.add(path)
        for neighbor in node.edges:
            seen.add(node)
            self.backtrack(neighbor, seen, path, paths)
            seen.remove(node)


class Node:
    def __init__(self, char: str):
        self.char = char
        self.edges = []
