class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        hulu = []
        cnt = 0
        num = A[0]
        for x in A:
            if x == num:
                cnt += 1
            else:
                hulu.append([num, cnt])
                cnt = 1
                num = x
        if cnt > 0:
            hulu.append([num, cnt])

        # print(hulu)

        output = 0

        if A[0] == 1:
            start = 0
        else:
            start = 1
            if len(hulu) < 2:
                return min(K, len(A))

        end = start

        usage = 0
        ones = hulu[start][1]
        while end + 2 < len(hulu) and usage + hulu[end + 1][1] <= K:
            usage += hulu[end + 1][1]
            ones += hulu[end + 2][1]
            end += 2

        output = ones + K

        # print([start,end,usage,ones])

        start += 2

        while start < len(hulu):
            ones -= hulu[start - 2][1]
            usage -= hulu[start - 1][1]
            if start > end:
                end = start
                ones = hulu[start][1]
                usage = 0
            while end + 2 < len(hulu) and usage + hulu[end + 1][1] <= K:
                usage += hulu[end + 1][1]
                ones += hulu[end + 2][1]
                end += 2
            # print([start,end,usage,ones])

            output = max(output, ones + K)
            start += 2

        return min(output, len(A))
