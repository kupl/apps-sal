class Solution:
    def power(self, number: int):
        count = 0
        while number > 1:
            if number % 2:
                number = 3 * number + 1
            else:
                number //= 2
            count += 1
        return count
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
        numbers_power = sorted([(self.power(number), number) for number in range(lo, hi + 1)])
        return numbers_power[k - 1][1]

