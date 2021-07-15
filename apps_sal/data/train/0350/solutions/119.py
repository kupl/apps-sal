class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        good_start, bad_start = -1, -1
        good_count, bad_count = {}, {}
        
        
        def add(count, element):
            if element not in count:
                count[element] = 0
            count[element] += 1

        def remove(count, element):
            count[element] -= 1
            if count[element] == 0:
                del count[element]      
    
        def find_good_start(A, K, cur_pos, index, good_count):
            if len(good_count) == K:
                return index
            cur = index
            while cur < cur_pos and len(good_count) > K:
                cur += 1
                remove(good_count, A[cur])
            return cur

        total = 0
        for i in range(len(A)):
            cur = A[i]
            add(good_count, cur)
            add(bad_count, cur)
            if len(good_count) >= K:
                good_start = find_good_start(A, K, i, good_start, good_count)
                bad_start = find_good_start(A, K-1, i, bad_start, bad_count)
                if len(good_count) == K and len(bad_count) == K-1:
                    total +=  bad_start - good_start
        return total
