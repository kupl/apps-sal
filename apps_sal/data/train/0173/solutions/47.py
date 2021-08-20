class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        bag = {}
        for i in arr:
            if i < 0:
                i += (-i // k + 1) * k
            r = i % k
            if r != 0:
                if k - r not in bag:
                    if r not in bag:
                        bag[r] = 0
                    bag[r] += 1
                else:
                    bag[k - r] -= 1
                    if bag[k - r] == 0:
                        del bag[k - r]
            elif 0 in bag:
                del bag[0]
            else:
                bag[0] = 1
        return len(bag) == 0
