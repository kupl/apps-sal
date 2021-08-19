class Solution:

    def can_ship(self, weights, D, max_weight):

        #print(weights, D)

        i = 0
        s = 0

        '''
        if len(weights)<D and max(weights)<=max_weight:
            return True
            
        if D==0 and len(weights)>0:
            return False

        if D==1 and sum(weights)<max_weight:
            return True

        while i<=len(weights)-1 and s<=max_weight:
            s+=weights[i]
            i+=1

        return self.can_ship(weights[i-1:], D-1, max_weight)
        '''

        while i < len(weights) and D > 0:

            s = 0

            while i < len(weights) and s <= max_weight:
                s += weights[i]

                if s > max_weight:
                    break

                i += 1

            D -= 1

            # print(\"test \", i, D, weights)

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

            # print(\"mid = \", mid, left, right)

            if right == left + 1:
                if self.can_ship(weights, D, left):
                    return left
                else:
                    return right

        return mid
