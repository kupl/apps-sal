

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        check_list = [0] * n

        for node in range(n):
            left_node = leftChild[node]
            right_node = rightChild[node]
            if left_node >= 0:
                check_list[left_node] += 1
            if right_node >= 0:
                check_list[right_node] += 1

        # print(check_list)
        # check if it's separated tree or there's mutual arrow
        zero_num = check_list.count(0)
        if zero_num != 1:
            return False
        if max(check_list) > 1:
            return False

        # check if it constructs binary tree
        root_node = check_list.index(0)
        check_list = [0] * n

        def check_binary_tree(node, check_list):
            check_list[node] += 1
            left_node = leftChild[node]
            right_node = rightChild[node]
            if left_node >= 0:
                check_binary_tree(left_node, check_list)
            if right_node >= 0:
                check_binary_tree(right_node, check_list)

        check_binary_tree(root_node, check_list)
        min_n, max_n = min(check_list), max(check_list)
        # print(check_list)
        if not (min_n == 1 and max_n == 1):
            return False

        return True
