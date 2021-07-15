class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # expected group len is equal to len(arr)
        if(m == len(arr)):
            return m
        '''
        group_edge = [0] * (len(arr)+2)
        ans = 0 
        for i in range(0, len(arr)):
            print(arr[i])
            left=right=arr[i]
            if group_edge[right+1]>0: 
                right=group_edge[right+1]
            if group_edge[left-1]>0: 
                left=group_edge[left-1]
            group_edge[left], group_edge[right] = right, left
            if (right-arr[i]==m) or (arr[i]-left ==m): 
                ans=i
            print(group_edge)
        '''
        group_len = [0] * (len(arr) + 2)
        cnt_group_len = [0] * (len(arr) + 1)
        ans = -1
        for i in range(0, len(arr)):
            
            #print(arr[i])
            
            left_most = arr[i] - 1
            right_most = arr[i] + 1
            new_len = group_len[left_most] + group_len[right_most] + 1
            group_len[arr[i]] = new_len
            
            cnt_group_len[new_len] += 1
            cnt_group_len[group_len[left_most]] -= 1
            cnt_group_len[group_len[right_most]] -= 1
            
            if(group_len[left_most] > 0):
                group_len[arr[i] - group_len[left_most]] = new_len
            
            if(group_len[right_most] > 0):
                group_len[arr[i] + group_len[right_most]] = new_len
            
            #print(group_len)
            #print(cnt_group_len)
            
            if(cnt_group_len[m] > 0):
                ans = i + 1
            
        return ans
                

