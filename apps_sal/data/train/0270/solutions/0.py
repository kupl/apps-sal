import math


class Solution:

    def __init__(self):
        self.happy_string = ''

    def getHappyString(self, n: int, k: int) -> str:
        poss_per_group = 2 ** (n - 1)
        group_num = math.ceil(k / poss_per_group) - 1
        starting_char = ''
        if k > poss_per_group * 3:
            return ''
        if group_num == 0:
            self.happy_string += 'a'
        elif group_num == 1:
            self.happy_string += 'b'
        else:
            self.happy_string += 'c'
        self.findNextChar(group_num, n - 1, group_num * poss_per_group, (group_num + 1) * poss_per_group, k)
        return self.happy_string

    def findNextChar(self, char_index: int, n: int, start: int, end: int, k: int) -> None:
        if n != 0:
            lower_index = -1
            upper_index = -1
            if char_index == 0:
                lower_index = 1
                upper_index = 2
            elif char_index == 1:
                lower_index = 0
                upper_index = 2
            else:
                lower_index = 0
                upper_index = 1
            midpoint = int((start + end) / 2)
            if k <= midpoint:
                self.happy_string += self.indexToStr(lower_index)
                self.findNextChar(lower_index, n - 1, start, midpoint, k)
            else:
                self.happy_string += self.indexToStr(upper_index)
                self.findNextChar(upper_index, n - 1, midpoint, end, k)

    def indexToStr(self, index: int) -> str:
        if index == 0:
            return 'a'
        elif index == 1:
            return 'b'
        else:
            return 'c'
