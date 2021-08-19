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
        (start, end, count) = (0, 0, len(t))
        (min_start, min_end) = (None, None)
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
                                (min_start, min_end) = (start, i)
                        table[s[start]] += 1
                    start += 1
        if min_start == None:
            return ''
        else:
            return s[min_start:min_end + 1]
        '\n         def check(m, n, mode=1):\n             table = dict(zip(t, [0]*len(t)))\n             for i in range(m, n+1):\n                 if s[i] in table:\n                     if mode == 1 and table[s[i]] != None:\n                         continue\n                     else:\n                         table[s[i]] = i\n \n             a, b = None, None\n             for k, v in table.items():\n                 if v == None:\n                     return 0, 0, False\n                 if a == None or a > v:\n                     a = v\n                 if b == None or b < v:\n                     b = v\n             return a, b, True\n         \n         first, last, result = check(0, len(s)-1, 1)\n         if not result:\n             return False\n         a, b = first, last\n         for i in range(last+1, len(s)):\n             t_a, t_b, result = check(i-(b-a+1), i, 2)\n             if result == True:\n                 a, b = t_a, t_b\n         \n         return s[a:(b+1)]\n         '
