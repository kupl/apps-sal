class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        # hashtable with dp
        
        res = 0
        mod = int(1e9+7)
        
        numbers = dict()
        sums = dict()
        
        for num in A:
            res = (res + sums.get(target - num, 0)) % mod
            
            for number, count in list(numbers.items()):
                sums[number + num] = sums.get(number+num, 0) + count
                
            numbers[num] = numbers.get(num, 0) + 1
            
        return res
            

