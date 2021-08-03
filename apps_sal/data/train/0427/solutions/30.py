class Solution:
    def countOrders(self, n: int) -> int:
        '''
Assume we have already n - 1 pairs, now we need to insert the nth pair.
To insert the first element, there are n * 2 - 1 chioces of position。
To insert the second element, there are n * 2 chioces of position。
So there are (n * 2 - 1) * n * 2 permutations.
Considering that delivery(i) is always after of pickup(i), we need to divide 2.
So it's (n * 2 - 1) * n.

        '''
        res = 1
        for i in range(2, n + 1):
            res = res * i * (2 * i - 1)
        return res % (10**9 + 7)
