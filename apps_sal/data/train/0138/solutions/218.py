
class Node:
    def __init__(self, size):
        self.size = size
        self.left = None
        self.right = None


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        nodes = []
        roots = []

        curr_size = 0
        prev = None

        for i in range(len(nums)):
            if nums[i] > 0:
                curr_size += 1
            else:
                node = Node(curr_size)
                nodes.append(node)
                if prev:
                    prev.right = node
                    node.left = prev
                else:
                    roots.append(node)
                if nums[i] != 0:
                    prev = node
                else:
                    prev = None
                curr_size = 0

        node = Node(curr_size)
        if prev:
            prev.right = node
            node.left = prev
        else:
            roots.append(node)

        # t_node = roots[0]
        # while t_node:
        #     print(t_node.size)
        #     t_node = t_node.right

        longest = 0
        for node in roots:
            first_count = node.size
            second_count = 0 if not node.right else node.right.size

            curr_node = node.right.right if node.right else None

            ind = 0

            while curr_node:
                if ind == 0:
                    first_count += curr_node.size + curr_node.left.size + 2
                    ind = 1
                else:
                    second_count += curr_node.size + curr_node.left.size + 2
                    ind = 0
                curr_node = curr_node.right

            # print(first_count)
            # print(second_count)
            longest = max(longest, first_count, second_count)

        return longest
