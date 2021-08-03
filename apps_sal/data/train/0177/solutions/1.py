class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = {}
        for c in t:
            table[c] = table[c] + 1 if c in table else 1
        start, end, count = 0, 0, len(t)
        min_start, min_end = None, None
        for i in range(len(s)):
            if s[i] in table:
                if table[s[i]] > 0:
                    count -= 1
                table[s[i]] -= 1
            if count == 0:
                while count == 0:
                    if s[start] in table:
                        if table[s[start]] >= 0:
                            count += 1
                            if min_start == None or i - start < min_end - min_start:
                                min_start, min_end = start, i
                        table[s[start]] += 1
                    start += 1
        if min_start == None:
            return ""
        else:
            return s[min_start:(min_end + 1)]

        '''
         def check(m, n, mode=1):
             table = dict(zip(t, [0]*len(t)))
             for i in range(m, n+1):
                 if s[i] in table:
                     if mode == 1 and table[s[i]] != None:
                         continue
                     else:
                         table[s[i]] = i
 
             a, b = None, None
             for k, v in table.items():
                 if v == None:
                     return 0, 0, False
                 if a == None or a > v:
                     a = v
                 if b == None or b < v:
                     b = v
             return a, b, True
         
         first, last, result = check(0, len(s)-1, 1)
         if not result:
             return False
         a, b = first, last
         for i in range(last+1, len(s)):
             t_a, t_b, result = check(i-(b-a+1), i, 2)
             if result == True:
                 a, b = t_a, t_b
         
         return s[a:(b+1)]
         '''
