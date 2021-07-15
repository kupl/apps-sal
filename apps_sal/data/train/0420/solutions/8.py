# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/578071/Python-Solution-Sliding-Window-(Easy-to-Read)
import collections 
class Solution:
    
    def findTheLongestSubstring(self, s: str) -> int:
        
        for substr_len in range(len(s), -1, -1): #dynamic sliding window []
            end_remove = len(s) - substr_len + 1 
            
            for start in range(end_remove):
                even = True #Let's assume everything is true so far (our code is going to try to break you)
                sub_str = s[start:start + substr_len]
                
                for vowel in 'aeiou': 
                    if sub_str.count(vowel) % 2 != 0:
                        even = False #means we're odd length c
                        break
                if even == True: #counter == 0 is saying all are odd 
                    return substr_len


# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         return recurseLongestSubstring(s)
        
# def recurseLongestSubstring(s):
#     # print(s)
#     a = e = i = o = u = 0
#     first_a = first_e = first_i = first_o = first_u = -1
#     last_a = last_e = last_i = last_o = last_u = -1

#     for index in range(0, len(s)):
#         if s[index] == 'a':
#             if first_a == -1:
#                 first_a = index
#             last_a = index
#             a += 1
#         elif s[index] == 'e':
#             if first_e == -1:
#                 first_e = index
#             last_e = index
#             e += 1
#         elif s[index] == 'i':
#             if first_i == -1:
#                 first_i = index
#             last_i = index
#             i += 1
#         elif s[index] == 'o':
#             if first_o == -1:
#                 first_o = index
#             last_o = index
#             o += 1
#         elif s[index] == 'u':
#             if first_u == -1:
#                 first_u = index
#             last_u = index
#             u += 1  
#     # print(a, e, i, o, u)
#     # print(first_a , first_e , first_i , first_o , first_u)
#     # print(last_a, last_e, last_i, last_o, last_u)
    
#     if all_even([a, e, i, o, u]):
#         return len(s)

#     pool = []    
#     if not is_even(a):
#         pool.append(recurseLongestSubstring(s[0:last_a]))
#         pool.append(recurseLongestSubstring(s[first_a + 1:len(s)]))
#     if not is_even(e):
#         pool.append(recurseLongestSubstring(s[0:last_e]))
#         pool.append(recurseLongestSubstring(s[first_e + 1:len(s)]))
#     if not is_even(i):
#         pool.append(recurseLongestSubstring(s[0:last_i]))
#         pool.append(recurseLongestSubstring(s[first_i + 1:len(s)]))
#     if not is_even(o):
#         pool.append(recurseLongestSubstring(s[0:last_o]))
#         pool.append(recurseLongestSubstring(s[first_o + 1:len(s)]))
#     if not is_even(u):
#         pool.append(recurseLongestSubstring(s[0:last_u]))
#         pool.append(recurseLongestSubstring(s[first_u + 1:len(s)]))
#     return max(pool)
    

# def all_even(nums):
#     for num in nums:
#         if not is_even(num):
#             return False
#     return True

# def is_even(num):
#     return num % 2 == 0

