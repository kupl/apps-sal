class Solution:

    def minJumps(self, arr: List[int]) -> int:
        A = arr
        n = len(A)
        q = []
        val_dic = collections.defaultdict(list)
        for (i, val) in enumerate(A):
            if len(val_dic[val]) > 0:
                last_range = val_dic[val][-1]
                if last_range[1] + 1 == i:
                    last_range[1] = i
                else:
                    val_dic[val].append([i, i])
            else:
                val_dic[val].append([i, i])
        walked_val = set()
        q.append(0)
        walked = set()
        steps = -1
        while len(q) > 0:
            cur_len = len(q)
            next_q = []
            for i in q:
                val = A[i]
                if i == n - 1:
                    return steps + 1
                walked.add(i)
                if i + 1 < n and i + 1 not in walked:
                    next_q.append(i + 1)
                if i - 1 > -1 and i - 1 not in walked:
                    next_q.append(i - 1)
                if val not in walked_val:
                    index_range_list = val_dic[val]
                    for index_range in index_range_list:
                        for j in (index_range[0], index_range[1]):
                            if j != i and j not in walked:
                                next_q.append(j)
                        walked_val.add(val)
            steps += 1
            q = next_q
        return steps
