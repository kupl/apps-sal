"""
'ab'
'ba'
1

'abc' -> 'acb' -> 'bca'
'bca'
2

'abac' -> 'baac' -> 'baca'
'baca'
2

'aabc' -> 'acba' -> 'abca'
'abca'
2

* See the problem as a graph problem.
* Nodes are the strings.
* Two nodes are conneted to each order if the one string is equal to the
  other if we swap two chars.
* The problem boils down to find the shortest path between A and B.
* Since this is an unweigthed graph, the shortest path can be found by
  traversing the graph in BFS.
  
  
'abc' -> 'bac'
      -> 'cba'
      -> 'acb'
      
* This approach doesn't sound an efficient approach because for every node
  we'd need to generated its adjcent nodes.
  
* This sounds like an optimization problem.

'abcd'  --> 'bcd'
'adbc'      'dbc'

* If the first char from A and B are equal, recurse on the remaining string.
* Else, swap A so it first char match and recurse. If the target char repeats,
  try swapping all of them and consider the one that leads to the smallest K.
  
  
('abac', 'baca') = 1 + ('aac', 'aca')
('aac', 'aca') = ('ac', 'ca')
('ac', 'ca') = 1 + ('a', 'a')
('a', 'a') = 0

"""


class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        return do_kSimilarity(list(A), list(B), {})


def do_kSimilarity(A, B, memo):
    if (tuple(A), tuple(B)) in memo:
        return memo[tuple(A), tuple(B)]
    if A == B:
        return 0
    if A[0] == B[0]:
        return do_kSimilarity(A[1:], B[1:], memo)
    else:
        swaps = []
        for (i, char) in enumerate(A):
            if char == B[0]:
                swaps.append(i)
        k = float('inf')
        for swap in swaps:
            (A[0], A[swap]) = (A[swap], A[0])
            k = min(k, 1 + do_kSimilarity(A[1:], B[1:], memo))
            (A[0], A[swap]) = (A[swap], A[0])
        memo[tuple(A), tuple(B)] = k
        return k
