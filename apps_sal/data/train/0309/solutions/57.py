class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        def dp_matrix_based():
            item_dict = collections.defaultdict(list)
            for i, x in enumerate(A):
                item_dict[x].append(i)

            C = max(A) - min(A)
            n = len(A)
            maxlen = -math.inf
            dp = [[-math.inf] * (2 * C + 1) for _ in range(n)]

            for i in range(n):
                dp[i][0 + C] = 1

            for i in range(n):
                for j in range(i + 1, n):
                    g = A[j] - A[i] + C
                    dp[j][g] = 2

            for i in range(1, n):
                for gap in range(2 * C + 1):
                    candidate = A[i] - gap + C
                    if candidate in item_dict:
                        for t in item_dict[candidate]:
                            if t < i:
                                dp[i][gap] = max(dp[i][gap], dp[t][gap] + 1)
                                maxlen = max(maxlen, dp[i][gap])

            return maxlen

        def dict_based():
            '''
            Less space and simpler
            '''

            dp = defaultdict(defaultdict)
            for i in range(len(A)):
                for j in range(i):
                    diff = A[i] - A[j]
                    if diff not in dp:
                        dp[diff] = {i: 2}
                    else:
                        dic = dp[diff]
                        if j not in dic:
                            dic[i] = 2
                        else:
                            dic[i] = dic[j] + 1
            maxlen = 0
            for k, v in list(dp.items()):
                for k1, v1 in list(v.items()):
                    maxlen = max(maxlen, v1)
            return maxlen
        return dict_based()
