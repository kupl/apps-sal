class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        type_cnt = {}
        max_fruit = -1
        left_ptr = 0
        last_cnt = 0
        while left_ptr < len(tree):
            right_ptr = left_ptr
            while right_ptr < len(tree) - 1 and tree[right_ptr] == tree[right_ptr + 1]:
                right_ptr += 1
            curr_type = tree[left_ptr]
            curr_cnt = right_ptr - left_ptr + 1

            if curr_type not in type_cnt:
                type_cnt[curr_type] = curr_cnt
            else:
                type_cnt[curr_type] += curr_cnt

            if len(type_cnt) > 2:
                type_cnt = {last_type: last_cnt, curr_type: curr_cnt}

            max_fruit = max(max_fruit, sum([cnt for cnt in list(type_cnt.values())]))
            last_cnt = curr_cnt
            last_type = curr_type
            left_ptr = right_ptr + 1
        return max_fruit
