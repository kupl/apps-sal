class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d = collections.Counter(A)
        if 0 in d:
          if d[0] & 1 == 1:
            return False
          d.pop(0)

        keys = sorted(d.keys())
        for i in keys:
          if i in d:
            if i < 0:
              if i / 2 not in d:
                return False
              if d[i] > d[i/2]:
                return False
              d[i/2] -= d[i]
              if d[i/2] == 0:
                d.pop(i/2)
              d.pop(i)
            else:
              if i * 2 not in d:
                return False
              if d[i] > d[i*2]:
                return False
              d[i*2] -= d[i]
              if d[i*2] == 0:
                d.pop(i*2)
              d.pop(i)
        return True

