class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        ans = {}
        
        for num in range(lo, hi + 1):
            num_copy = num
            steps = 0
            while num_copy != 1:
                if num_copy % 2 == 0:
                    num_copy = num_copy / 2
                    steps += 1
                else:
                    num_copy = 3 * num_copy + 1
                    steps += 1
            ans[num] = steps
        
        return(sorted(list(ans.items()), key=lambda item: item[1]))[k-1][0]

