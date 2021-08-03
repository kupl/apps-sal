class Solution():
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(speed) -> bool:
            # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
            return sum((pile - 1) // speed + 1 for pile in piles) <= H  # faster

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

# SELF TRY 10/7/2020
# class Solution:
#     def minEatingSpeed(self, piles: List[int], H: int) -> int:
#         def eat_speed(K, H):
#             banana_per_hour = 0 #This is basically the hour it'll take to eat all the bananas.
#             #Let's say K = 4
#             #Pile is 10
#             #To eat 4 per hour it takes 3 hours
#             #You can do pile // K -> 10 // 4 = 2  (8 banana in 2 hours)
#             #Then pile % K -> 2 remainder is 2 (so since k is 4 then we can eat all the bananas)
#             for pile in piles:
#                 banana_per_hour += pile // K
#                 if pile % K != 0: #You can eat all of it takes an extra hour only
#                     banana_per_hour += 1
#             return banana_per_hour


#         #inclusive this is what we use for our K value to TRY
#         left = 1
#         right = max(piles)

#         while left <= right:
#             K = left + (right - left) // 2
#             banana_per_hour = eat_speed(K,H)
#             if banana_per_hour <= H: #this is fine
#                 right = K - 1
#             else: #banana_per_hour > H #not possible so we need to increase the number of bananas that Koko can eat.
#                 left = K + 1
#         return left


# class Solution:
#     def minEatingSpeed(self, piles: List[int], H: int) -> int:


#         def K_speed(K, piles):
#             hours_to_eat = 0

#             for pile in piles:
#                 hours_to_eat = hours_to_eat + (pile // K)
#                 if pile % K != 0:
#                     hours_to_eat += 1


#                 # if pile % K == 0:

#             return hours_to_eat

#         #two cases
#         # 1 < H
#         #2 == H
#         left = 1
#         right = max(piles)
#         #other way is inclusive ^
#         #but left <= right
#         # and if that's the case right = K - 1
#         #So if you do it <= you know that AT that point hours to eat is <= H we know that there's a possibility of our CURRENT K being a solution
#         #However in this case you need to do a K - 1 because you are trying to find the next smallest for Koko still eating all bananas.
#         #Because if our RIGHT becomes < our right we are done
#         while left < right:
#             K = left + (right - left) // 2
#             if K_speed(K, piles) <= H:
#                 right = K

#             else:
#                 left = K + 1


#         # LEFT has passed your RIGHT BOUND
#         #inclsuvie or exclusive inclsuive w/ one exclusive
#         #I give you a number that doesn't exist
#         return left


#     #BINARY SEARCH
#     LEFT <= RIGHT:


#         return LEFT whatever it is your answer

        # monkey eats bananas
        # there are N piles of bananas
        # the i-th pile has piles[i] amount of bananas
        # The guard have gone and will come back in H hours

        # She has a bananas eating per hour speed K
        # Each hour she chosses some banans and eats the K bannas in that pile

#         1)
        # If the pile has less than K bananas she eats all of them
        # And won't eat anymore bananas during the hour

        # Monkey eats slow but needs to finish eating all the bananas before the guard comes back

        # Return the minimum (int) K s.t she can eat all the bananas within H hours.

        #
        # K to try to eat all the piles within that hour
