class Solution:
     def originalDigits(self, s):
         """
         :type s: str
         :rtype: str
         """
         
         order_c = ['w', 'u', 'x', 'g', 'z', 'o', 't', 'f', 'v', 'i']
         order_d = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]
         cl = [list(e) for e in ['tow', 'four', 'six', 'eight', 'zero', 'one', 'three', 'five', 'seven', 'nine']]
         digit_cnt = [0] * 10
         
         counter = dict()
         for c in s:
             counter[c] = counter.get(c, 0) + 1
             
         for i in range(len(order_c)):
             cnt = counter.get(order_c[i], 0)
             digit_cnt[order_d[i]] = cnt
             
             if cnt > 0:
                 for c in cl[i]:
                     counter[c] -= cnt
                     
         ans = list()
         for i in range(len(digit_cnt)):
             if digit_cnt[i] > 0:
                 ans.append(('%d' % i) * digit_cnt[i])
                        
         return ''.join(ans)
