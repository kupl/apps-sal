class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        diffs = set(y - x for i, x in enumerate(A) for y in A[i + 1:])
        ans = 0
        for diff in diffs:
            data = {}
            for num in A:
                if num - diff not in data:
                    if num not in data:
                        data[num] = [num]
                    continue
                if len(data[num - diff]) < len(data.get(num, [])):
                    continue
                seq = data.pop(num - diff)
                seq.append(num)
                ans = max(ans, len(seq))
                data[num] = seq
        return ans
