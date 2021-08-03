class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        bit = [None] * (len(arr) + 1)
        res = -1
        step = 1
        group = 0
        for i in range(len(arr)):
            #print(step, arr[i], group)
            temp = 1
            right = 0
            left = 0
            # print(bit)
            if arr[i] - 1 > 0 and bit[arr[i] - 1] != None:
                if bit[arr[i] - 1] == 'True':
                    bit[arr[i] - m] = False
                    bit[arr[i] - 1] = False
                    bit[arr[i]] = False
                    group -= 1
                elif bit[arr[i] - 1] == False:
                    bit[arr[i]] = False
                else:
                    right += bit[arr[i] - 1]

            if arr[i] + 1 <= len(arr) and bit[arr[i] + 1] != None:

                if bit[arr[i] + 1] == 'True':
                    bit[arr[i] + m] = False
                    bit[arr[i] + 1] = False
                    bit[arr[i]] = False
                    group -= 1
                elif bit[arr[i]] == False:
                    if bit[arr[i] + 1]:
                        bit[arr[i] + bit[arr[i] + 1]] = False
                    bit[arr[i] + 1] = False
                elif bit[arr[i] + 1] == False:
                    bit[arr[i]] = False
                else:
                    left += bit[arr[i] + 1]
            if bit[arr[i]] == None:
                #print(arr[i],right , left)
                temp += right + left
                bit[arr[i]] = temp
                if right:
                    bit[arr[i] - right] += left + 1
                if left:
                    bit[arr[i] + left] += right + 1
                if temp == m:
                    bit[arr[i] - right] = 'True'
                    bit[arr[i] + left] = 'True'
                    group += 1
            # print(bit)
            if group > 0:
                res = step
            step += 1
        return res
