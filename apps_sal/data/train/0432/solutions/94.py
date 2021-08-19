class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k:
            return False
        Ct = Counter(nums)
        heapify(nums)

        if len(Ct) > len(nums) * 0.75:
            return self.isNStraightHand(nums, k)

        while Ct:
            start = heappop(nums)
            while not Ct[start]:
                start = heappop(nums)
            for i in range(start, start + k):
               # print(num+i)
                if not Ct[i]:
                    return False
                if Ct[i] == 1:
                    del Ct[i]
                else:
                    Ct[i] -= 1

        return True

    def isNStraightHand(self, hand, W):
      #  heapify(hand)

        while hand:
            last_item = heappop(hand)
            leftover = []

            for _ in range(W - 1):
                if not hand:
                    return False
                next_item = heappop(hand)

                while next_item == last_item:
                    leftover.append(next_item)
                    if not hand:
                        return False
                    next_item = heappop(hand)

                if next_item > last_item + 1:
                    return False
                last_item = next_item
            for item in leftover:
                heappush(hand, item)

        return True
