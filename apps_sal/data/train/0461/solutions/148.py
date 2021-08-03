class RelationTree:
    def __init__(self, e_id, time):
        self.e_id = e_id
        self.time = time
        self.subs = []


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        relation_dict = collections.defaultdict(list)
        for i, m_id in enumerate(manager):
            relation_dict[m_id].append(i)
        self.max_time = 0

        def createTree(e_id, cum_time):
            curr_root = RelationTree(e_id, informTime[e_id])
            if curr_root.time:
                for sub_id in relation_dict[e_id]:
                    curr_root.subs.append(createTree(sub_id, cum_time + curr_root.time))
            else:
                self.max_time = max(self.max_time, cum_time)
            return curr_root
        root = createTree(headID, 0)

        return self.max_time
