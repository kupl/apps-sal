class Solution:

    def maxRepOpt1(self, text: str) -> int:
        groups = []
        for (key, group) in itertools.groupby(text):
            groups.append([key, len(list(group))])
        count = collections.Counter(text)
        for index in range(len(groups)):
            if index <= len(groups) - 3:
                if groups[index + 1][1] == 1 and groups[index + 2][0] == groups[index][0]:
                    groups[index][1] += groups[index + 2][1]
            if count[groups[index][0]] > groups[index][1]:
                groups[index][1] += 1
        maxlength = 0
        for group in groups:
            if group[1] > maxlength:
                maxlength = group[1]
        return maxlength
