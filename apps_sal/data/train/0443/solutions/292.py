class Solution:

    def checkList(self, head, tail, init: int) -> int:
        result = init
        head_copy = head.copy()
        for i in head_copy:
            num = tail[0]
            ilen = len(i)
            if ilen > 0:
                if ilen == 2:
                    if i[0] < i[1] and i[1] < num:
                        result += 1
                    if i[0] > i[1] and i[1] > num:
                        result += 1
                elif ilen == 1:
                    head.append(i + [num])
            else:
                head.append([num])
        if len(tail) == 1:
            return result
        else:
            del tail[0]
            return self.checkList(head, tail, result)

    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        list = [[]]
        return self.checkList(list, rating, 0)
