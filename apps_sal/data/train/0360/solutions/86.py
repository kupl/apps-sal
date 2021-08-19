class Solution:

    def can_ship(self, weights, D, max_weight):
        i = 0
        s = 0
        '\n        if len(weights)<D and max(weights)<=max_weight:\n            return True\n            \n        if D==0 and len(weights)>0:\n            return False\n\n        if D==1 and sum(weights)<max_weight:\n            return True\n\n        while i<=len(weights)-1 and s<=max_weight:\n            s+=weights[i]\n            i+=1\n\n        return self.can_ship(weights[i-1:], D-1, max_weight)\n        '
        while i < len(weights) and D > 0:
            s = 0
            while i < len(weights) and s <= max_weight:
                s += weights[i]
                if s > max_weight:
                    break
                i += 1
            D -= 1
        if D == 0 and i < len(weights):
            return False
        return True

    def shipWithinDays(self, weights, D):
        left = min(weights)
        right = sum(weights)
        while left < right:
            mid = int((left + right) / 2)
            if self.can_ship(weights, D, mid):
                right = mid
            else:
                left = mid
            if right == left + 1:
                if self.can_ship(weights, D, left):
                    return left
                else:
                    return right
        return mid
