class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def helper(boss_to_sub, informTime, start):
            return informTime[start] + max((helper(boss_to_sub, informTime, i) for i in boss_to_sub[start])) if boss_to_sub[start] else 0
        boss_to_sub = defaultdict(list)
        for (i, m) in enumerate(manager):
            boss_to_sub[m].append(i)
        del boss_to_sub[-1]
        return helper(boss_to_sub, informTime, headID)
