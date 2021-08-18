class Solution:
    def countOrders(self, n: int) -> int:
        orderResults = {}

        def orderHelper(pickupsLeft, heldPackages):
            key = (pickupsLeft, heldPackages)
            if key in orderResults:
                return orderResults[key]

            if key == (0, 0):
                return 0
            elif key == (0, 1):
                return 1
            elif key == (1, 0):
                return 1

            res = 0
            if pickupsLeft > 0:
                res += pickupsLeft * orderHelper(pickupsLeft - 1, heldPackages + 1)
            if heldPackages > 0:
                res += heldPackages * orderHelper(pickupsLeft, heldPackages - 1)
            res = res % (10**9 + 7)

            orderResults[key] = res
            return res

        return orderHelper(n, 0)
