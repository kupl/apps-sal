class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        count = defaultdict(int)
        left = {}
        right = {}
        lastStep = -1
        for step, n in enumerate(arr):
            i = n-1
            # print('----')
            # print(step, i)
            newLeft = i
            newRight = i

            if i > 0:
                if i-1 in right:
                    newLeft = right[i-1]
                    del right[i-1]
                    count[i-newLeft] -= 1
            if i < N-1:
                if i+1 in left:
                    newRight = left[i+1]
                    del left[i+1]                    
                    count[newRight-i] -= 1


            left[newLeft] = newRight
            right[newRight] = newLeft
            count[newRight - newLeft + 1] += 1
            # print('left:',left)
            # print('right:',right)
            # print('count:',count)
            if count[m] > 0:
                lastStep = step + 1

        return lastStep
