class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s = set()
        prev = set()
        prev.add(arr[0])
        s.add(arr[0])
                        
        for i in range(len(arr)):
            temp = set()
            for val in prev:
                temp.add(val|arr[i])
                s.add(val|arr[i])
                
            prev = temp
            prev.add(arr[i])
            s.add(arr[i])
        
        return len(s)
