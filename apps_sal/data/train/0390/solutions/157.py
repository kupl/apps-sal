class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # This is an even simpler and more efficient way to reason about the state of 
        # f(x). Instead of defining f(x) for whether Alice wins or loses, let f(x)
        # return True/False for if someone, Alice or Bob wins/loses given the value x.
        # In other words, f(x) tells us whether we'll win or lose if we start with x.
        # If \"we\" are Alice starting with x, then our opponent is Bob, if \"we\" are
        # Bob then the opponent is Alice.
        memo = {}
        def f(x):
            if x == 0:
                return False
            if x == 1:
                return True
            
            if x in memo:
                return memo[x]
            
            i = 1
            while i * i <= x:
                # If we choose to remove i*i and our opponent ends up losing then
                # we win. Why? Since we are playing optimally, as long as there's a
                # choice we can make that forces the opponent to lose, we will make
                # that choice and guarantee the win.
                if f(x - i * i) == False:
                    memo[x] = True
                    return True
                i += 1
            
            # If no matter the choice we make, our opponent ends up winning, i.e
            # f(x - i * i) == True for all i, i*i <= x, then we are guaranteed to lose
            memo[x] = False
            return False
        
        return f(n)
            

