'''

brute force - 2 for loops, find diff of i and i+1, then find next elem j where j-(i+i) is the same
keep track of max len found
  t=O(n^3)
  s=O(1)



[20,1,15,3,10,5,8]
                {}
              {3:2}
           {-5:2,-2:2}
         {7:2,2:2,5:2}
      {-12:2,-5:3,-10:2,-7:2}
    
                

  |       |
0,1,0,1,0,1
          {}
        {1:2}
      {-1:2, 0:2}
    {1:2,0:2}
  {-1:2,0:3,}
max = 4
-19


'''


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        maps = [{} for i in range(len(A))]
        maxlen = 0
        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if diff in maps[j]:
                    length = maps[j][diff] + 1
                else:
                    length = 2
                maxlen = max(maxlen, length)
                if diff in maps[i]:
                    prev_max = maps[i][diff]
                    maps[i][diff] = max(prev_max, length)
                else:
                    maps[i][diff] = length
        return maxlen


def search(vals, start, target, length):
    for i in range(start + 1, len(vals)):
        if vals[i] - vals[start] == target:
            return search(vals, i, target, length + 1)
    return length
