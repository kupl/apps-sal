class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        (result, sLen, numW, wLen) = ([], len(s), len(words), len(words[0]))
        if sLen < numW * wLen:
            return []
        dic = collections.defaultdict(int)
        for i in words:
            dic[i] += 1
        for i in range(wLen):
            (left, count) = (i, 0)
            tmp = collections.defaultdict(int)
            for j in range(i, sLen - wLen + 1, wLen):
                s1 = s[j:j + wLen]
                if s1 in dic:
                    tmp[s1] += 1
                    if tmp[s1] <= dic[s1]:
                        count += 1
                    else:
                        while tmp[s1] > dic[s1]:
                            s2 = s[left:left + wLen]
                            tmp[s2] -= 1
                            if tmp[s2] < dic[s2]:
                                count -= 1
                            left += wLen
                    if count == numW:
                        result.append(left)
                        tmp[s[left:left + wLen]] -= 1
                        count -= 1
                        left += wLen
                else:
                    (tmp, count, left) = (collections.defaultdict(int), 0, j + wLen)
        return result
