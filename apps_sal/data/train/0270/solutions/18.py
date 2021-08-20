import math
LETTER_SET = ['a', 'b', 'c']
LEFT = 0
RIGHT = 1


class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        index = self.getRootIndex(n, k)
        if index == None:
            return ''
        kth_happy = LETTER_SET[index]
        happy_strings_per_node = self.calculateTotalNumOfHappyForN(n)
        min_range = happy_strings_per_node * index + 1
        max_range = happy_strings_per_node * (index + 1)
        for level in range(n - 1):
            direction = self.findDirection(min_range, max_range, k)
            kth_happy = self.nextHappyString(kth_happy, direction)
            (min_range, max_range) = self.fetchNewRange(min_range, max_range, direction)
        return kth_happy

    def findDirection(self, min_range, max_range, k):
        min_low = min_range
        min_high = math.floor((min_range + max_range) / 2)
        max_low = min_high + 1
        max_high = max_range
        is_in_min_range = k >= min_low and k <= min_high
        return LEFT if is_in_min_range else RIGHT

    def fetchNewRange(self, min_range, max_range, direction):
        min_low = min_range
        min_high = math.floor((min_range + max_range) / 2)
        max_low = min_high + 1
        max_high = max_range
        return (min_low, min_high) if LEFT == direction else (max_low, max_high)

    def calculateTotalNumOfHappyForN(self, n):
        return 2 ** (n - 1)

    def getRootIndex(self, n, k):
        happy_strings_total = self.calculateTotalNumOfHappyForN(n) * len(LETTER_SET)
        happy_strings_per_node = happy_strings_total / len(LETTER_SET)
        for i in range(len(LETTER_SET)):
            min_range = happy_strings_per_node * i + 1
            max_range = happy_strings_per_node * (i + 1)
            if k >= min_range and k <= max_range:
                return i
        return None

    def nextHappyString(self, string, direction):
        happyStrings = []
        for letter in LETTER_SET:
            if self.isValidHappyString(string, letter):
                happyStrings.append(string + letter)
        return happyStrings[direction]

    def isValidHappyString(self, string, letter):
        return string[-1] != letter
