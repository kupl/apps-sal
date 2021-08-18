class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = []
        n = len(rating)

        def btInc(index: int, curr: List[int]):
            if len(curr) == 3:
                res.append(curr)
                return

            for i in range(index + 1, n):
                if curr == [] or rating[i] > curr[-1]:
                    btInc(i, curr + [rating[i]])

        def btDec(index: int, curr: List[int]):
            if len(curr) == 3:
                res.append(curr)
                return

            for i in range(index + 1, n):
                if curr == [] or rating[i] < curr[-1]:
                    btDec(i, curr + [rating[i]])

        btInc(-1, [])
        btDec(-1, [])

        return len(res)
