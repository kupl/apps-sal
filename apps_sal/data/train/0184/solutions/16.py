class Solution:
    def maxRepOpt1(self, text: str) -> int:

        if not text:
            return 0

        compact = [[text[0], 1]]
        max_ = 1

        for i in range(1, len(text)):
            if text[i] == compact[-1][0]:
                compact[-1][1] += 1
            else:
                compact.append([text[i], 1])
            max_ = max(max_, compact[-1][1])

        last_idx = defaultdict(int)

        for i in range(len(compact)):
            last_idx[compact[i][0]] += compact[i][1]

        # print(compact)

        for i in range(len(compact) - 2):

            if compact[i][0] == compact[i + 2][0] and compact[i + 1][1] == 1 and compact[i][1] + compact[i + 2][1] < last_idx[compact[i][0]]:
                max_ = max(max_, compact[i][1] + compact[i + 2][1] + 1)

            if compact[i][0] == compact[i + 2][0] and compact[i + 1][1] == 1:
                max_ = max(max_, compact[i][1] + compact[i + 2][1])

        for i in range(len(compact)):
            if last_idx[compact[i][0]] > compact[i][1]:
                max_ = max(max_, compact[i][1] + 1)

        return max_
