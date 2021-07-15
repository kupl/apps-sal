'''
Using BFS

Idea and Facts

Another Reference:
https://leetcode.com/problems/escape-a-large-maze/discuss/282870/python-solution-with-picture-show-my-thoughts
https://assets.leetcode.com/users/2017111303/image_1556424333.png

FAQ
Question I think the maximum area is 10000?
Answer
The maximum area is NOT 10000. Even it's accepted with bound 10000, it's WRONG.
The same, the bfs with just block.size steps, is also wrong.

In the following case, the area is 19900.
The sum of the area available equals 1+2+3+4+5+...+198+199=(1+199)*199/2=19900 (trapezoid sum) --> Area = B*(B-1)/2
X -> blocking points

0th      _________________________
         |O O O O O O O X
         |O O O O O O X
         |O O O O O X
         |O O O O X
         .O O O X
         .O O X
         .O X
200th    |X

Question I think the maximum area is area of a sector.
Answer
All cells are discrete, so there is nothing to do with pi.


Question What is the maximum area?
Answer
It maximum blocked is achieved when the blocked squares,
surrounding one of the corners as a 45-degree straight line.

And it's easily proved.

If two cells are connected horizontally,
we can slide one part vertically to get bigger area.

If two cells are connected vertically,
we can slide one part horizontally to get bigger area.


Question Can we apply a BFS?
Answer
Yes, it works.
BFS in 4 directions need block.length * 2 as step bounds,
BFS in 8 directions need block.length as step bounds.

It needs to be noticed that,
The top voted BFS solution is WRONG with bound,
though it's accpected by Leetcode.

But compared with the complexity:
Searching with limited area is O(0.5B*B).
BFS with steps can be O(2B^B).


Intuition
Simple search will get TLE, because the big search space.
Anyway, we don't need to go further to know if we are blocked or not.
Because the maximum area blocked are 19900.


Explanation
Search from source to target,
if find, return true;
if not find, return false;
if reach 20000 steps, return true.

Then we do the same thing searching from target to source.

Complexity
Time complexity depends on the size of blocked
The maximum area blocked are B * (B - 1) / 2.
As a result, time and space complexity are both O(B^2)
In my solution I used a fixed upper bound 20000.
'''
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        blocked = set(map(tuple, blocked))
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def bfs(s, t):
            bfsQ = [tuple(s)]
            visited = {tuple(s)}
            areaSum = 0
            
            for x, y in bfsQ:
                for i,j in dirs:
                    r = x+i
                    c = y+j
                    
                    if 0 <= r < 10**6 and 0 <= c < 10**6 and (r,c) not in visited and (r,c) not in blocked:
                        if (r,c) == tuple(t):
                            return True
                        bfsQ.append((r,c))
                        visited.add((r,c))
                        
                if len(bfsQ) >= 20000: # max block area upper bound
                    return True
            
            return False
    
        return bfs(source, target) and bfs(target, source)
