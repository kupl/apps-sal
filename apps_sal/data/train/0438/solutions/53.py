class Solution:

    def findLatestStep(self, a: List[int], m: int) -> int:
        index2len = defaultdict(int)
        cnt = Counter()
        last = -1
        for (i, p) in enumerate(a):
            (left_len, right_len) = (index2len[p - 1], index2len[p + 1])
            new_len = left_len + 1 + right_len
            index2len[p - left_len] = index2len[p + right_len] = new_len
            cnt[left_len] -= 1
            cnt[right_len] -= 1
            cnt[new_len] += 1
            if cnt[m] > 0:
                last = i + 1
        return last
