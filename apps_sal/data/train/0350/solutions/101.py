class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        sum = 0
        begin = 0
        end = 0
        s = collections.defaultdict(int)
        lA = len(A)
        for i in range(lA):
            if len(s) >= K:
                s[A[i]] += 1
                if s[A[i]] > 1:
                    newend = end
                    while s[A[newend]] > 1:
                        s[A[newend]] -= 1
                        newend += 1
                    end = newend
                else:
                    begin = end
                    while s[A[begin]] > 1:
                        s[A[begin]] -= 1
                        begin += 1
                    s[A[begin]] -= 1
                    begin += 1
                    end = begin
                    while s[A[end]] > 1:
                        s[A[end]] -= 1
                        end += 1
                sum += end - begin + 1
            else:
                s[A[i]] += 1
                if len(s) == K:
                    while s[A[end]] > 1:
                        s[A[end]] -= 1
                        end += 1
                    sum += end - begin + 1
        return sum
