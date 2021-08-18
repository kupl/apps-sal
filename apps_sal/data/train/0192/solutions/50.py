class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        st = deque(piles)
        mySum = 0
        while len(st) > 0:
            left = st.popleft()
            right = st.pop()
            urs = st.pop()
            mySum += urs

        return mySum
