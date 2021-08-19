class Solution:

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        hash = {}
        res = []
        wsize = len(words[0])
        for str in words:
            if str in hash:
                hash[str] += 1
            else:
                hash[str] = 1
        for start in range(0, len(words[0])):
            slidingWindow = {}
            wCount = 0
            for i in range(start, len(s), wsize):
                word = s[i:i + wsize]
                if word in hash:
                    if word in slidingWindow:
                        slidingWindow[word] += 1
                    else:
                        slidingWindow[word] = 1
                    wCount += 1
                    while hash[word] < slidingWindow[word]:
                        pos = i - wsize * (wCount - 1)
                        removeWord = s[pos:pos + wsize]
                        slidingWindow[removeWord] -= 1
                        wCount -= 1
                else:
                    slidingWindow.clear()
                    wCount = 0
                if wCount == len(words):
                    res.append(i - wsize * (wCount - 1))
        return res
