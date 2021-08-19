class Solution:
    def findLUSlength(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

   #    public CONCISE solution....beat 95%

        def issubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)

        for s in sorted(A, key=len, reverse=True):
            if sum(issubsequence(s, t) for t in A) == 1:
                return len(s)
        return -1

        """
         def issub(w1, w2):
             i = 0
             for w in w2:
                 if i < len(w1) and w1[i] == w:
                     i += 1
             return i == len(w1)
         
         A.sort(key = len, reverse = True)
         for s in A:
             A_copy = A.copy()
             A_copy.remove(s)
             if all(not issub(s, ss) for ss in A_copy):
                 return len(s)
         return -1
         """

        """
         def subseq(w1, w2):
             #True if word1 is a subsequence of word2.
             i = 0
             for c in w2:
                 if i < len(w1) and w1[i] == c:
                     i += 1
             return i == len(w1)
     
         A.sort(key = len, reverse = True)
         for i, word1 in enumerate(A):
             if all(not subseq(word1, word2) 
                     for j, word2 in enumerate(A) if i != j):
                 return len(word1)
         return -1
         
         
         
         
         
         
         When we add a letter Y to our candidate longest uncommon subsequence answer of X, 
         it only makes it strictly harder to find a common subsequence.
         Thus our candidate longest uncommon subsequences will be chosen from the group of words itself.
 
         Suppose we have some candidate X. 
         We only need to check whether X is not a subsequence of any of the other words Y. 
         To save some time, we could have quickly ruled out Y when len(Y) < len(X), 
         either by adding “if len(w1) > len(w2): return False” or enumerating over A[:i] (and checking neighbors for equality.) 
         However, the problem has such small input constraints that this is not required.
 
         We want the max length of all candidates with the desired property, 
         so we check candidates in descending order of length. 
         When we find a suitable one, we know it must be the best nonlocal answer.
         """
