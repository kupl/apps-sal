class Solution:

    def findLUSlength(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def issubsequence(s, t):
            t = iter(t)
            return all((c in t for c in s))
        for s in sorted(A, key=len, reverse=True):
            if sum((issubsequence(s, t) for t in A)) == 1:
                return len(s)
        return -1
        '\n         def issub(w1, w2):\n             i = 0\n             for w in w2:\n                 if i < len(w1) and w1[i] == w:\n                     i += 1\n             return i == len(w1)\n         \n         A.sort(key = len, reverse = True)\n         for s in A:\n             A_copy = A.copy()\n             A_copy.remove(s)\n             if all(not issub(s, ss) for ss in A_copy):\n                 return len(s)\n         return -1\n         '
        '\n         def subseq(w1, w2):\n             #True if word1 is a subsequence of word2.\n             i = 0\n             for c in w2:\n                 if i < len(w1) and w1[i] == c:\n                     i += 1\n             return i == len(w1)\n     \n         A.sort(key = len, reverse = True)\n         for i, word1 in enumerate(A):\n             if all(not subseq(word1, word2) \n                     for j, word2 in enumerate(A) if i != j):\n                 return len(word1)\n         return -1\n         \n         \n         \n         \n         \n         \n         When we add a letter Y to our candidate longest uncommon subsequence answer of X, \n         it only makes it strictly harder to find a common subsequence.\n         Thus our candidate longest uncommon subsequences will be chosen from the group of words itself.\n \n         Suppose we have some candidate X. \n         We only need to check whether X is not a subsequence of any of the other words Y. \n         To save some time, we could have quickly ruled out Y when len(Y) < len(X), \n         either by adding “if len(w1) > len(w2): return False” or enumerating over A[:i] (and checking neighbors for equality.) \n         However, the problem has such small input constraints that this is not required.\n \n         We want the max length of all candidates with the desired property, \n         so we check candidates in descending order of length. \n         When we find a suitable one, we know it must be the best nonlocal answer.\n         '
