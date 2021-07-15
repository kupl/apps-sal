class Solution:
  def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    # TC: O(MNNT), SC: (NT)
    # dp: (n-color, t-blocks): min-cost
    dp0, dp1 = {(0, 0): 0}, {}
    for i, k in enumerate(houses):
      # assume painted houses can NOT be repainted..
      for ik in ([k] if k > 0 else range(1, n + 1)):
        # previous color and blocks
        for pk, pb in dp0:
          bb = pb + (ik != pk)
          if bb > target:
            continue
          dp1[ik, bb] = min(dp1.get((ik, bb), float('inf')), dp0[pk, pb] + (0 if k > 0 else cost[i][ik - 1]))
      dp0, dp1 = dp1, {}
    return min([dp0[k, b] for k, b in dp0 if b == target] or [-1])
