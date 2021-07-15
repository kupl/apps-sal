class Solution:
    ''' greedy approach. start from the left side, 
\t    and everytime pick the smallest number on the right side that is able to swap, then do the swap
    '''
    def minInteger(self, num: str, k: int) -> str:
        min_num = sorted(list(num))
        min_num = ''.join(min_num)
        i = 0
        to_find = 0
        while num != min_num and k > 0 and i < len(num):
            indx = num.find(str(to_find), i)
            while indx != -1:
                if indx - i <= k:   # able to swap
                    num = num[:i] + num[indx] + num[i:indx] + num[indx+1:]  # the swap
                    k -= (indx - i)
                    i += 1
                    to_find = 0     # restart the to_find variable
                    indx = num.find(str(to_find), i)
                else:
                    break
            to_find += 1
        return num
