class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        counter = collections.defaultdict(int)
        count = collections.defaultdict(int)
        ans = -1
        term = 1
        for i in arr:
            if i - 1 in counter and i + 1 in counter:
                left_most = counter[i - 1]
                right_most = counter[i + 1]
                counter[left_most] = right_most
                counter[right_most] = left_most
                count[right_most - left_most + 1] += 1
                count[i - left_most] -= 1
                count[right_most - i] -= 1
                if i - 1 != left_most:
                    del counter[i - 1]
                if i + 1 != right_most:
                    del counter[i + 1]
            elif i - 1 in counter:
                left_most = counter[i - 1]
                counter[left_most] = i
                counter[i] = left_most
                count[i - left_most] -= 1
                count[i - left_most + 1] += 1
                if i - 1 != left_most:
                    del counter[i - 1]
            elif i + 1 in counter:
                right_most = counter[i + 1]
                counter[right_most] = i
                counter[i] = right_most
                count[right_most - i] -= 1
                count[right_most - i + 1] += 1
                if i + 1 != right_most:
                    del counter[i + 1]
            else:
                counter[i] = i
                count[1] += 1
            if m in count and count[m] > 0:
                ans = term
            term += 1
        return ans
