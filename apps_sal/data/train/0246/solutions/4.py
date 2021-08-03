class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence + ' '
        dic = {}
        for i in dict:
            if i[0] not in list(dic.keys()):
                dic[i[0]] = [i]
            else:
                dic[i[0]].append(i)
        res = ''
        while len(sentence) > 0:
            word = sentence[:sentence.index(' ')]
            tmp = ''
            if word[0] in list(dic.keys()):
                for refer in dic[word[0]]:
                    if len(refer) < len(word):
                        if word[:len(refer)] == refer:
                            if tmp == '':
                                tmp = refer
                            else:
                                if len(tmp) > len(refer):
                                    tmp = refer
            if tmp != '':
                res += tmp + ' '
            else:
                res += word + ' '
            sentence = sentence[sentence.index(' ') + 1:]
        res = res[:-1]
        return res
