# O(n) time and space
# Hashmap and array
# Count number then count occurrence:
# Count the occurrences of each number using HashMap;
# Keep a count of different occurences
# From small to big, for each unvisited least frequent element, deduct from k the multiplication with the number of elements of same occurrence, check if reaching 0, then deduct the corresponding unique count remaining.
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        distinct = len(freq)
        freq_count = collections.Counter(list(freq.values()))
        
        idx = 1
        while k>0:
            if k - idx*freq_count[idx] >= 0:
                k -= idx*freq_count[idx]
                distinct -= freq_count[idx]
                idx += 1
            else:
                # can't remove all, but can remove partially
                # [2,4,1,8,3,5,1,3], 3
                return distinct - k // idx
        return distinct
                
        

