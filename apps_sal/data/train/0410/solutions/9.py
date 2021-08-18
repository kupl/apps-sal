class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        count = 0
        answers = []
        numbers = []
        memo = {}
        for number in range(lo, hi + 1):
            original = number
            numbers.append(numbers)
            count = 0
            while number != 1:
                if number % 2 == 0:
                    number = number // 2
                    count = count + 1
                else:
                    number = 3 * number + 1
                    count = count + 1
            memo[original] = count

        sort_memo = sorted(list(memo.items()), key=lambda x: x[1], reverse=False)
        return sort_memo[k - 1][0]
