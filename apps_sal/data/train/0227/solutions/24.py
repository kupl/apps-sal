class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        subarrays = []
        start = -1
        i = 0
        while i < len(A):
            if A[i] == 1:
                if start == -1:
                    start = i
            else:
                if start != -1:
                    subarrays.append([start, i])
                    start = -1
            i += 1
        if A[i - 1] == 1:
            subarrays.append([start, i])
        print(subarrays)

        if K == 0:
            result = 0
            for arr in subarrays:
                if arr[1] - arr[0] > result:
                    result = arr[1] - arr[0]
            return result

        window = []
        start = []
        end = []
        result = 0
        for i in range(len(A)):
            if A[i] == 0:
                if len(window) == K:
                    window.pop(0)
                window.append(i)
                left = window[0] - 1
                right = window[-1] + 1
                while left >= 0 and A[left] != 0:
                    left -= 1
                while right < len(A) and A[right] != 0:
                    right += 1
                if right - left > result:
                    result = right - left
                # for i in range(start, len(subarrays)):
                #     if subarrays[i][0] > window[0]:
                #         break
                #     start = i
                # for i in range(len(subarrays)-1, end-1, -1):
                #     if subarrays[i][1] < window[-1]:
                #         break
                #     end = i

        # result = 0
        # for curr_k in range(K, 0, -1)
        #     i = 0
        #     while i < len(subarrays) - 1:
        #         gap = subarrays[i][1] + subarrays[i][0] - 1
        #         if gap == curr_k:
        return result - 1
