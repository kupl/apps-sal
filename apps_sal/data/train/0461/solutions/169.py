class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        man_idx = [[man, idx] for idx, man in enumerate(manager)]
        man_copy = [[man, idx] for idx, man in enumerate(manager)]
        max_time = 0
        curr_time = 0
        memo_table = {}
        start = man_idx[-1][1]
        while man_idx:
            curr_man = man_idx.pop()
            if curr_man[1] in memo_table:
                curr_time += memo_table[curr_man[1]]
                memo_table[start] = curr_time
                max_time = max(max_time, curr_time)
                if len(man_idx) > 0:
                    start = man_idx[-1][1]
                curr_time = 0
                continue
            curr_time += informTime[curr_man[1]]
            if curr_man[0] == -1:
                max_time = max(max_time, curr_time)
                memo_table[start] = curr_time
                if len(man_idx) > 0:
                    start = man_idx[-1][1]
                curr_time = 0
            else:
                man_idx.append(man_copy[curr_man[0]])
        return max_time
