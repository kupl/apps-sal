from collections import defaultdict


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = defaultdict(int)
        for n in arr:
            mod = n % k
            complement = (k - mod) % k
            if counter.get(complement, 0):
                counter[complement] -= 1
            else:
                counter[mod] += 1
        return all((v == 0 for v in counter.values()))
