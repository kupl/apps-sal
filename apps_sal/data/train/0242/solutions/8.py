from collections import Counter, defaultdict

class Solution:
  def maxEqualFreq(self, nums: List[int]) -> int:
    counter = Counter(nums)
    # d: count -> values has such counts
    d = defaultdict(set)
    for x in counter:
      d[counter[x]].add(x)
    # O(n), reverse go through nums updating count of counts
    n = len(nums)
    while d:
      if len(d) == 1:
        k = list(d.keys())[0]
        if k == 1 or len(d[k]) == 1:
          return n
      if len(d) == 2:
        y, z = sorted(d.keys())
        if (y == 1 and len(d[y]) == 1) or (y + 1 == z and len(d[z]) == 1):
          return n
      n -= 1
      # update counter and count of counts
      x = nums[n]
      d[counter[x]].remove(x)
      if not d[counter[x]]:
        d.pop(counter[x])
      counter[x] -= 1
      if counter[x] > 0:
        d[counter[x]].add(x)
    return 0

