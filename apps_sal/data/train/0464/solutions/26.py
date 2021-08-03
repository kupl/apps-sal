class Solution:
    def minOperations(self, n: int) -> int:

        sum_tot = 0
        for i in range(n):
            val = 2 * i + 1
            # print(val)
            if val > n:
                sum_tot += val - n
            else:
                sum_tot += n - val

        return(int(sum_tot / 2))

        '''
        if n%2  == 0:
            median = int((arr[int(n/2)] + arr[int(n/2)-1])/2)
        else:
            median = arr[int(n/2)]
        print(median)
        
        ctr = 0
        while(len(set(arr)) > 1):
            min_elem = arr[-1] + 1
            max_elem = -1
            min_ind = -1
            max_ind = -1
            for i in range(len(arr)):
                if arr[i] > max_elem:
                    max_elem = arr[i]
                    max_ind = i
                if arr[i] < min_elem:
                    min_elem = arr[i]
                    min_ind = i
            arr[max_ind] -= 1
            arr[min_ind] += 1
            ctr += 1
        
        return ctr
        '''
