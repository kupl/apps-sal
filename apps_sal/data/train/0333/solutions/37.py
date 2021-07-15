class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # BFS
        A = arr
        n = len(A)
        q = []
        val_dic = collections.defaultdict(list)
        for i, val in enumerate(A):
            if len(val_dic[val]) > 0:
                last_range = val_dic[val][-1]
                if last_range[1]+1 == i:
                    last_range[1] = i
                else:
                    val_dic[val].append([i,i])
            else:
                val_dic[val].append([i,i])
                
        walked_val = set()
        # for i in val_dic[A[0]]:
        q.append(0)
            
        walked = set()
        steps = -1
        while len(q) > 0:
            # print(q)
            cur_len = len(q)
            next_q = []
            for i in q:
                val = A[i]
                if i == n-1:
                    return steps+1
                
                walked.add(i)
                
                if i+1 < n and i+1 not in walked:
                    next_q.append(i+1)
                if i-1 > -1 and i-1 not in walked:
                    next_q.append(i-1)
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



# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         # BFS
#         A = arr
#         n = len(A)
#         q = collections.deque()
#         val_dic = collections.defaultdict(list)
#         for i, val in enumerate(A):
#             if len(val_dic[val]) > 0:
#                 last_range = val_dic[val][-1]
#                 if last_range[1]+1 == i:
#                     last_range[1] = i
#                 else:
#                     val_dic[val].append([i,i])
#             else:
#                 val_dic[val].append([i,i])
                
#         walked_val = set()
#         # for i in val_dic[A[0]]:
#         q.append(0)
            
#         walked = set()
#         steps = -1
#         while len(q) > 0:
#             # print(q)
#             cur_len = len(q)
#             for _ in range(0,cur_len):
                
#                 i = q.popleft()
#                 val = A[i]
#                 if i == n-1:
#                     return steps+1
                
#                 walked.add(i)
                
#                 if i+1 < n and i+1 not in walked:
#                     q.append(i+1)
#                 if i-1 > -1 and i-1 not in walked:
#                     q.append(i-1)

#                 # 不要去遍历和自己的值相同的元素，如果不便利，就增加不进去。
#                 # 如果这个值已经被遍历过了，就不要再次遍历。
                
#                 if val not in walked_val:
#                     index_range_list = val_dic[val]
#                     for index_range in index_range_list:
#                         for j in (index_range[0], index_range[1]):
#                             if j != i and j not in walked:
#                                 q.append(j)
#                         walked_val.add(val)
                
#             steps += 1
                
#         return steps

