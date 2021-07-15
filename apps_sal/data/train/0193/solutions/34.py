class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = dict()
        # count all distinct values
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
            
        #greedy solution
        #sort counts in desc order
        total_count=0        
        for index, count in enumerate(sorted(list(counts.values()), reverse=True)):
            total_count += count
            if total_count >= len(arr) // 2:
                return index + 1
        return 0

