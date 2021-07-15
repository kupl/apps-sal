class Solution:
    def isArrSorted(self, a) -> tuple((bool, bool)):
        is_exp_sorted = True
        is_eq_sorted = True

        for i, l in enumerate(a):
            if i == len(a) - 1:
                break
            
            if not l < a[i+1]:
                is_exp_sorted = False
            if not l <= a[i+1]:
                is_eq_sorted = False
        return (is_exp_sorted, is_eq_sorted)

    def minDeletionSize(self, A: List[str]) -> int:
        deletion_count = 0
        
        built_A = [''] * len(A)
        
        for i in range(0, len(A[0])):
            letters_at_i = [s[i] for s in A]
            is_exp_sorted, is_eq_sorted = self.isArrSorted(letters_at_i)
            # print(is_exp_sorted, is_eq_sorted)
            
            if is_exp_sorted:
                break
            
            test_A = [built_A[oi] + o[i] for oi, o in enumerate(A)]
            # print(test_A)
            if list(sorted(test_A)) == test_A:
                built_A = test_A
                continue
            else:
                deletion_count += 1
        
        return deletion_count

