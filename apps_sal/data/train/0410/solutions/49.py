class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(x):
          count = 0
          while(x != 1):
            if (x % 2 == 0):
              x /= 2
              count += 1
            else:
              x = 3 * x + 1
              count += 1
          return count
        dic = {}
        for i in range(lo, hi+1):
          dic[i] = getPower(i)
        
        sorted_dic = sorted(list(dic.items()), key = lambda x: x[1], reverse=False)
        print(sorted_dic)
        for i in range(len(sorted_dic)):
          if (i == k-1):
            return sorted_dic[i][0]
        
        
        
        

