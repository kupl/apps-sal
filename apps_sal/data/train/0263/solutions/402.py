class Solution:
    def knightDialer(self, n: int) -> int:
      moves = {
        0: [4, 6],
        2: [7, 9],
        1: [6, 8],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
      }        
      
      store = {}
      def f(num, rem):
        if rem == 1: return 1 
        if (num, rem) in store: return store[(num, rem)]
        res = store[(num, rem)] = sum([f(m, rem - 1) for m in moves[num]])
        return res
      
      return sum([f(num, n) for num in range(10)]) % (10 ** 9 + 7)
        
        
        
        
      

