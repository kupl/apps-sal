class Track(object):
    def __init__(self, n=2):
        self.count = {}

        self.last = {}
        self.order = [None for _ in range(n - 1)]

    def is_new_elem(self, elem):
        return elem not in self.count

    def is_last_elem(self, elem):
        return elem in self.last

    def add(self, elem):
        if self.is_new_elem(elem):
            self.count = {elem: 1}
            for key, val in self.last.items():
                self.count[key] = val
        else:
            self.count[elem] += 1

        if self.is_last_elem(elem):
            self.last[elem] += 1
        else:
            if elem in self.order:
                del self.order[self.order.index(elem)]
            else:
                rem = self.order.pop(0)
                if rem is not None:
                    del self.last[rem]

            self.last[elem] = 1
            self.order.append(elem)

    def get_count(self):
        total = 0
        for _, val in self.count.items():
            total += val
        return total


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        tracker = Track()

        max_count = 0
        for t in tree:
            tracker.add(t)
            max_count = max(max_count, tracker.get_count())

        return max_count
