class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        from operator import itemgetter
        result = []
        letter_to_feq = defaultdict(lambda: 0)
        feq_to_letter = defaultdict(list)
        for c in s:
            letter_to_feq[c] += 1
        max_count = -1
        for k, v in letter_to_feq.items():
            feq_to_letter[v].append(k)
            if v > max_count:
                max_count = v
        for i in range(max_count, 0, -1):
            if i in feq_to_letter:
                for c in feq_to_letter[i]:
                    result = result + [c] * i
        return ''.join(result)
        '''hashmap = defaultdict(lambda: 0)
         for c in s:
             hashmap[c] += 1
         for k, v in sorted(hashmap.items(), key=itemgetter(1), reverse=True):
             result = result + [k] * v
         return ''.join(result)'''
