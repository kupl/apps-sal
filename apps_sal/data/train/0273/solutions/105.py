class Solution:

    def racecar(self, tgt: int) -> int:
        '''
            shortest path -> bfs

            starting from [0, 1], how to reach tgt = 5?

                [0, 1] -> [1, 2], [0, -1]

                    [1, 2] -> [3, 4], [1, -1]
                    [0, -1] ->[-1, -2], [0, 1] ... visited


                        [3, 4] -> [3, -1], [7, 8]
                        [1,-1] -> [0, -2], [1, 1]
                        [-1,-2]-> [-3,-4] ... too far, [-1,1]


                            [3, -1] -> [2, -2], [3, 1]
                            [7,  8] ... too far
                            [0, -2] -> [-2, -4] ... too far, [0, 1] ... visited
                            [1,  1] -> [2, 2], [1, -1] ...visited
                            [-1 ,1] -> [0, 2], [-1, -1] ... too far


                                [2, -2] -> [0, -4], [2, 1]
                                [3,  1] -> [4,  2], [3, -1] ... visited
                                [2,  2] -> [4,  4], [2, -1]
                                [0,  2] -> [2,  4], [0, -1] ... visited

                                    [0, -4] -> [-4, -8] ... too far, [0, 1] ... visited
                                    [2,  1] -> [3,   2], [2, -1]
                                    [4,  2] -> [6,   4], [4, -1]
                                    [4,  4] -> [8,   8], [4, -1] ... in queue
                                    [2, -1] -> [1,  -2], [2,  1] ... visited
                                    [2,  4] -> [6,   8], [2, -1] ... visited


                                        [3, 2] -> [5 , 4]  -->> arrived

                                        -> 7 steps                                    
        '''

        '''
            1. try greedy -> can't pass tgt = 5
            
            2. list out all the step until reach the tgt -> time: O(2 ^ (num of operations) )
            
            3. speed up -> dont visit same nodes, dont go to \"too far\" nodes    
                        
            4. time complexity: 
                pos range: -tgt ~ tgt, spd range: 1 ~ log(tgt) -> graph node number will be 2 * tgt * log(tgt) -> O(tgt * log(tgt) )
                                                
        '''

        visited = dict()
        q = collections.deque()

        q.append([0, 1])
        visited[0] = set()
        visited[0].add(1)

        step = 0
        while len(q) > 0:

            curSize = len(q)

            for i in range(0, curSize):

                pop = q.pop()
                pos, spd = pop[0], pop[1]

                if pos == tgt:
                    return step

                nextSteps = [[pos + spd, spd * 2], [pos, - 1 * spd // abs(spd)]]
                for nextStep in nextSteps:

                    nPos, nSpd = nextStep[0], nextStep[1]

                    if abs(nPos - tgt) <= tgt:
                        if nPos not in visited or nSpd not in visited[nPos]:
                            q.appendleft(nextStep)
                            if nPos not in visited:
                                visited[nPos] = set()

                            visited[nPos].add(nSpd)

            step += 1

        return -1
