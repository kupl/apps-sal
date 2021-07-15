class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        N = len(tree)
        oneidx = twoidx = 0
        onetype = tree[0]
        twotype = None
        left, right = 0, 0
        while right < N and tree[right] == onetype:
          oneidx += 1
          right += 1
        oneidx -= 1
        if right == N:
          return N
        twotype = tree[right]
        twoidx = right
        while right < N:
          if tree[right] == onetype:
            oneidx = right
          elif tree[right] == twotype:
            twoidx = right
          else:
            res = max(res, right - left)
            if oneidx < twoidx:
              left = oneidx + 1
              onetype = tree[right]
              oneidx = right
            else:
              left = twoidx + 1
              twotype = tree[right]
              twoidx = right
          right += 1
        return max(res, right - left)

