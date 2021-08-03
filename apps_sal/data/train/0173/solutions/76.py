class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        rem = collections.Counter()
        for a in arr:
            rem[a % k] += 1

        for a in arr:
            one = a % k
            if rem[one] == 0:
                continue
            rem[one] -= 1
            two = one if one == 0 else k - one
            if rem[two] == 0:
                return False
            rem[two] -= 1
        return True
