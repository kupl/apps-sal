class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        curr_list = []
        smaller = []
        larger = []

        def find_insertion(ele):
            left = 0
            right = len(curr_list)
            while left < right:
                middle = (left + right) // 2
                if curr_list[middle] < ele:
                    left = middle + 1
                else:
                    right = middle
            return left
        for i in range(1, len(A) + 1):
            index = find_insertion([A[-i], len(A) - i])
            if index < len(curr_list) and curr_list[index][0] == A[-i]:
                smaller.append(curr_list[index][1])
                larger.append(curr_list[index][1])
                curr_list[index][1] = len(A) - i
            else:
                if index > 0:
                    smaller.append(curr_list[index - 1][1])
                else:
                    smaller.append(None)
                if index < len(curr_list):
                    larger.append(curr_list[index][1])
                else:
                    larger.append(None)
                curr_list.insert(index, [A[-i], len(A) - i])
        smaller.reverse()
        larger.reverse()
        can_reach_odd = [False] * len(A)
        can_reach_even = [False] * len(A)
        can_reach_odd[-1] = True
        can_reach_even[-1] = True
        for i in range(2, len(A) + 1):
            if larger[-i] != None:
                can_reach_odd[-i] = can_reach_even[larger[-i]]
            if smaller[-i] != None:
                can_reach_even[-i] = can_reach_odd[smaller[-i]]
        solution = 0
        for i in can_reach_odd:
            if i:
                solution += 1
        return solution
