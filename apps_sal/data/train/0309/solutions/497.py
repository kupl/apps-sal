class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        for diff in range(-500, 501):
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
