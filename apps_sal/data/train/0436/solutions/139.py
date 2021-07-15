class Solution:
    def minDays(self, n: int) -> int:
        day = 0
        options = set([n])
        while 0 not in options:
            new_options = set()
            day += 1
            for o in options:
                new_options.add(o - 1)
                if not o % 2:
                    new_options.add(o // 2)
                if not o % 3:
                    new_options.add(o // 3)
            options = set(new_options)
        return day
        

