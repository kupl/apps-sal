class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        st = deque(piles)
        mySum = 0
        while len(st) > 0:
            # print(st)
            left = st.popleft()
            right = st.pop()
            urs = st.pop()
            # print(left, urs, right)
            mySum += urs
            

        # print(st)
        return mySum
