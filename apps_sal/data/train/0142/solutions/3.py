class Solution:

    def findLUSlength(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        '\n    #    a public CONCISE solution....\n    \n         def issubsequence(s, t):\n             t = iter(t)\n             return all(c in t for c in s)\n     \n         for s in sorted(strs, key=len, reverse=True):\n             if sum(issubsequence(s, t) for t in strs) == 1:\n                 return len(s)\n         return -1\n         '

        def subseq(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)
        A.sort(key=len, reverse=True)
        for (i, word1) in enumerate(A):
            if all((not subseq(word1, word2) for (j, word2) in enumerate(A) if i != j)):
                return len(word1)
        return -1
        '\n         When we add a letter Y to our candidate longest uncommon subsequence answer of X, \n         it only makes it strictly harder to find a common subsequence.\n         Thus our candidate longest uncommon subsequences will be chosen from the group of words itself.\n \n         Suppose we have some candidate X. \n         We only need to check whether X is not a subsequence of any of the other words Y. \n         To save some time, we could have quickly ruled out Y when len(Y) < len(X), \n         either by adding “if len(w1) > len(w2): return False” or enumerating over A[:i] (and checking neighbors for equality.) \n         However, the problem has such small input constraints that this is not required.\n \n         We want the max length of all candidates with the desired property, \n         so we check candidates in descending order of length. \n         When we find a suitable one, we know it must be the best nonlocal answer.\n         '
