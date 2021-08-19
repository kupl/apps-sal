class Solution:
    def knightDialer(self, n: int) -> int:
        # recursive backtracking:
        # you have 4 options:
        #     (2 right, 1 down)
        #     (2 right, 1 up)
        #     (2 left, 1 down)
        #     (2 left, 1 up)
        # we have a grid, 4 by 3
        if n == 1:
            return 10
        # grid = [
        #     [1, 2, 3],
        #     [4, 5, 6],
        #     [7, 8, 9],
        #     [-1,0,-1]
        # ]
        # # append the number after reaching node
        # # we could do dynamic programming and remember how many we can reach if
        # # we are at a specific n
        # # at 0,0:
        # # we can create a graph of things we can connect,
        # # ie how many things can we reach from where we are right now

        # 0 - 9 are the connections
        maps = {
            0: {4, 6},
            1: {6, 8},
            2: {7, 9},
            3: {4, 8},
            4: {3, 9, 0},
            5: {},
            6: {1, 7, 0},
            7: {2, 6},
            8: {1, 3},
            9: {4, 2}
        }
        prev = [1] * 10
        for i in range(1, n):
            curr = [0] * 10
            for j in range(0, 10):
                curr[j] = sum(prev[k] for k in maps[j])
            prev = curr
        return sum(prev) % (10**9 + 7)

        '''
            this index is the sum of all previous possibilities
            we see when we reach at index 1, there are 2 places we could have came from
            we have n total moves and 9 total numbers
            we start at number 1, number 1 is connected to 6 and 8
            now we go to 6 and 8,
                6 connected to 1, 0, 7
                8 connected to 1, 3
                
                can we some how sum for each n?
                opt(i, j) = sum(opt(i-1, j) for j in connected )
                return the sum of the top part of the array
                
                
                
                n=2 [1= arr[i-1][6]+arr[i-1][[8] ... ]]
                n=1 [1:1, 2:1, 3:1 ... 0:1]
            
        
        '''


#         count = 0
#         numbers = set()
#         def recursion(x, y, number, depth):
#             nonlocal count, numbers
#             if depth > n:
#                 return
#             if not(0<= x < 4 and 0<=y<3 and grid[x][y]!=-1):
#                 return
#             if depth == n:
#                 numbers.add(number)
#                 return
#             else:
#                 number+=grid[x][y]*(10**depth)
#                 recursion(x+2, y-1, number, depth+1)
#                 recursion(x+2, y+1, number, depth+1)

#                 recursion(x-2, y-1, number, depth+1)
#                 recursion(x-2, y+1, number, depth+1)

#                 recursion(x+1, y+2, number, depth+1)
#                 recursion(x+1, y-2, number, depth+1)

#                 recursion(x-1, y+2, number, depth+1)
#                 recursion(x-1, y-2, number, depth+1)

#                 return
#         for x in range(0, 4):
#             for y in range(0, 3):
#                 recursion(x, y, 0, 0)
#         print(numbers)
#         return len(numbers)%(10**9+7)
