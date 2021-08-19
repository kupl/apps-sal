from sortedcontainers import SortedDict


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1
        dp_even, dp_odd = [False] * (n + 1), [False] * (n + 1)

#         even_jumps, odd_jumps = [-1]*n, [-1]*n
#         asc_sorted = sorted((val,i) for i,val in enumerate(A))
#         desc_sorted = sorted((-val,i) for i,val in enumerate(A))
#         # odd jumps
#         stack = deque()
#         for val, i in asc_sorted:
#             while stack and stack[-1] < i:
#                 odd_jumps[stack.pop()] = i
#             stack.append(i)
#         # even jumps
#         stack = deque()
#         for val, i in desc_sorted:
#             while stack and stack[-1] < i:
#                 even_jumps[stack.pop()] = i
#             stack.append(i)

        dp_even[n - 1] = dp_odd[n - 1] = True
#         for i in reversed(range(n-1)):
#             dp_even[i] = dp_odd[even_jumps[i]]
#             dp_odd[i] = dp_even[odd_jumps[i]]
#         return dp_odd.count(True)
        sortedDict = SortedDict({A[n - 1]: n - 1})
        for i in reversed(range(n - 1)):
            num = A[i]
            # Find rightmost value less than or equal to num
            lower = sortedDict.bisect_right(num)
            lower = sortedDict[sortedDict.keys()[lower - 1]] if lower else -1
            # Find leftmost item greater than or equal to num
            higher = sortedDict.bisect_left(num)
            higher = -1 if higher == len(sortedDict) else sortedDict[sortedDict.keys()[higher]]
            # print('lower', lower)
            # print('higher', higher)
            # print('sortedDict', sortedDict)
            sortedDict[num] = i
            dp_even[i] = dp_odd[lower]
            dp_odd[i] = dp_even[higher]
        # print('dp_odd', dp_odd)
        # print('dp_even',dp_even)
        return dp_odd.count(True)
