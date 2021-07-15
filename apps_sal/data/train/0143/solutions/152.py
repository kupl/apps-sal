class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not len(tree):
            return 0
        count_max = 0
        start = 0
        f_num = tree[0]
        tracking = set()
        tracking.add(f_num)
        last_change = 0
        current_num = tree[0]
        for i in range(1, len(tree)):
            if tree[i] not in tracking:
                if len(tracking) >= 2:
                    count_max = max(i-start, count_max)
                    tracking.remove(f_num)
                    tracking.add(tree[i])
                    f_num = current_num
                    start = last_change
                    
                else:
                    tracking.add(tree[i])
            if tree[i] != current_num:
                last_change = i
                f_num = current_num
                current_num = tree[i]
        count_max = max(len(tree)-start, count_max)
        return count_max

                
                

