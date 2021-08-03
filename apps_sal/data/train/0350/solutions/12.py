class Solution:
    def subarraysWithKDistinct(self, s: List[int], K: int) -> int:
        obj = defaultdict(int)
        first = 0
        second = 0
        answer = 0
        for i in range(len(s)):
            obj[s[i]] += 1
            if len(obj) == K + 1:
                # remove the distinct at second, move second, first
                del obj[s[second]]
                second += 1
                first = second
            if len(obj) == K:
                # update second and answer (Notice: K >= 1)
                while obj[s[second]] > 1:
                    obj[s[second]] -= 1
                    second += 1
                answer += second - first + 1

        return(answer)
