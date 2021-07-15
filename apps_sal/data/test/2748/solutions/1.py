class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         if not digits:
             return []
         MAPPING = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
         def directed_combinations(i, partial):
             if i == len(digits):
                 result.append(''.join(partial))
                 return
             
             for c in MAPPING[int(digits[i])]:
                 directed_combinations(i + 1, partial + [c])
         
         result = []
         directed_combinations(0, [])
         return result
