class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = 0
        right = 0
        window = set()
        res = 0
        last_index = collections.defaultdict(int)
        
        while left < len(tree) and right < len(tree):
            fruit_type = tree[right]
            last_index[fruit_type] = right
            if tree[right] in window or len(window) < 2:
                window.add(tree[right])
            else:
                window.add(tree[right])
                while len(window) > 2:
                    fruit_type = tree[left]
                    if left == last_index[fruit_type]:
                        window.remove(fruit_type)
                    left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

