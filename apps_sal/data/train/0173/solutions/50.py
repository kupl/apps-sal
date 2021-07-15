class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # int arr and integer k
        # divide array into pairs such that the sum of each pair is divisible by k
        # return True if possible, other false
        
        # [1, 2, 3, 4, 5, 10, 6, 7, 8, 9] k = 5   5, 10, 15, 20, 25, 30
        #  4  3  2
        #  9  8  7
        # 14 13 12
        # elem = 1 poss: 4, 9 k%5 == 4  
        # elem = 2 poss: 3, 8 k%5 == 3
        # elem = 3 poss: 2, 7 k%5 == 2
        # elem = 4 poss: 1, 6 k%5 == 1
        # elem = 5 poss: 10   k%5 == 0
        # elem = 6 poss: 4, 9
        # elem = 7 poss: 3, 8 # see if there are any pairs that have not been matched yet. if so, check their possible matches and see if one is available
        # elem = 8 poss: 2, 7
        # elem = 9 poss: 1, 6
        # elem = 10 poss: 5
        
        # arr = [1,2,3,4,5,6], k = 10
        # elem = 1 poss: x
        
        
        # 1 - 4 6 - 9 
        # 1 - 9 4 - 6
        
        # 2 - 3 8 - 7 
        # 2 - 8 3 - 7
        
        # 5 - 10
        modFrequencies = {}
        for i in range(0, len(arr)):
            difference = arr[i] % k
            if difference not in modFrequencies:
                modFrequencies[difference] = 0
            modFrequencies[difference] += 1
            
        for mod in modFrequencies:
            if mod == 0:
                if modFrequencies[mod] % 2 == 1: 
                    return False
            elif k-mod not in modFrequencies or modFrequencies[mod] != modFrequencies[k-mod]:
                return False
        return True
            
            
            
        

