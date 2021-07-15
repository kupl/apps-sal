
from functools import reduce
class Solution:
    
    validMoves = {
        0: {4, 6},
        1: {6, 8},
        2: {7, 9},
        3: {4, 8},
        4: {3, 9, 0},
        5: {},
        6: {1, 7, 0},
        7: {2, 6},
        8: {1, 3},
        9: {2, 4}
    }
    
    def knightDialer(self, n: int) -> int:
        cache = {} # from (remainingMoves, location) => numberOfPaths
        
        def reducer(acc: int, x: int) -> int:
            return (acc + x) % 1000000007 #10^9+7
        
        def helper(remainingMoves: int, location: int) -> int:
            depth = n - remainingMoves
            insert = '\\t' * depth
            # print('{}ENTER: at {} with {} remaining'.format('\\t' * (depth - 1), location, remainingMoves))
            
            if remainingMoves == 0:
                # print('{}Ran out of moves in location {}'.format(insert, location))
                return 1
            else:
                if (remainingMoves, location) in cache:
                    answer = cache[(remainingMoves, location)]
                    # print('{}Found ({}, {}) in cache: returning {}'.format(insert, remainingMoves, location, answer))
                    return answer
                else:
                    nextMoves = self.validMoves[location]
                    answers = [helper(remainingMoves - 1, newLocation) for newLocation in nextMoves]
                    reduced = reduce(reducer, answers, 0)
                    cache[(remainingMoves, location)] = reduced
                    # print('{}Calculated ({}, {}) = {}'.format(insert, remainingMoves, location, reduced))
                    return reduced
        
        answers = [helper(n-1, x) for x in range(0, 10)]
        reduced = reduce(reducer, answers, 0)
        return reduced
