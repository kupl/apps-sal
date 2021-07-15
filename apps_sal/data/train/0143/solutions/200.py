class Solution(object):
    def totalFruit(self, tree):
        n = len(tree)
        left, right = 0, 0
        basket = {}
        
        ans = 0
        while right<n:
            while left<right and len(basket)>1:
                basket.update({tree[left]:basket.get(tree[left], 0)-1})
                if basket.get(tree[left], None) == 0:
                    basket.pop(tree[left])
                left +=1
                
            basket.update({tree[right]:basket.get(tree[right], 0)+1})
            right += 1
            while right<n and basket.get(tree[right], 0) > 0:
                basket.update({tree[right]:basket.get(tree[right], 0)+1})
                right += 1
            # print(left, right, basket)
            ans = max(ans, right-left)
        return ans
