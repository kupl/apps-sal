class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # https://www.youtube.com/watch?v=8ttxdMCU2GE
        m = len(arr1)
        # remove dulpicates and sort arr2
        arr2 = sorted(list(set(arr2)))
        # print(arr2)
        n = len(arr2)
        swap = [[float('inf') for j in range(n)] for i in range(m)]
        keep = [float('inf') for i in range(m)]

        # initialization
        keep[0] = 0
        for j in range(n):
            swap[0][j] = 1

        for i in range(1, m):
            min_keep = float('inf')
            min_swap = float('inf')
            for j in range(n):
                # two variables to help compute case 3 & 4
                # case 4: the last two elements of current valid array are both from arr2
                if j > 0:
                    min_swap = min(min_swap, swap[i - 1][j - 1] + 1)

                # case 3: the second to last element is replaced by the previous element arr2[j-1] or earlier elements
                if arr1[i] > arr2[j]:
                    min_keep = min(min_keep, swap[i - 1][j])

                # case 1: no need to swap; keep arr1[i]
                if arr1[i] > arr1[i - 1]:
                    keep[i] = keep[i - 1]

                # case 2: ## replace arr1[i] by arr2[j]
                if arr2[j] > arr1[i - 1]:
                    swap[i][j] = keep[i - 1] + 1

                # update
                swap[i][j] = min(swap[i][j], min_swap)
                keep[i] = min(keep[i], min_keep)

        # for i in range(m):
        #     print(keep[i], swap[i])

        res = min(min(swap[m - 1]), keep[m - 1])
        if res == float('inf'):
            return -1
        else:
            return res
