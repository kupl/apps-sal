class Solution:
    def minNumberOfFrogs(self, croak: str) -> int:
        if len(croak) == 0:
            return 0
        if croak[0] != 'c':
            return -1
        if len(croak) % 5 != 0:
            return -1
        arr = [0 for _ in range(6)]
        arr[0] = 9999999
        index = {'c':1, 'r':2, 'o':3, 'a':4, 'k':5}
        
        for letter in croak:
            i = index[letter]            
            if arr[i-1] > 0:
                if i == 1 and arr[5]:
                    arr[5] -= 1
                arr[i-1] -= 1
                arr[i] += 1
            else:
                return -1
        for i in arr[1:-1]:
            if i != 0:
                return -1
        return arr[-1]
