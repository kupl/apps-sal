class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        i = 1
        l_max = A[i-1]

        d = Counter(A[i:])
        a_dict = OrderedDict(sorted(d.items()))
        r_min = next(iter(a_dict.items()))[0]

        while l_max > r_min:
            i += 1
            l_max = max(l_max, A[i-1])
            if a_dict[A[i-1]] > 1:
                a_dict[A[i-1]] -= 1
            else:
                del a_dict[A[i-1]]
                r_min = next(iter(a_dict.items()))[0]
                
        return i
