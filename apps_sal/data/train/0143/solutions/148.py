class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        deq = []
        currentTwo = set()
        result = 0
        temp = 0
        for e in tree:
            if len(deq) == 0:
                currentTwo.add(e)
                deq.append((e, 1))
                temp = 1
            elif e in currentTwo:
                if e == deq[-1][0]:
                    deq[-1] = (e, deq[-1][1] + 1)
                    temp += 1
                else:
                    deq.append((e, 1))
                    temp += 1
            else:
                previousOne = deq[-1][0]
                currentTwo = set([previousOne, e])
                deq = deq[-1:]
                temp = deq[-1][1]
                deq.append((e, 1))
                temp += 1

            result = max(result, temp)

        return result
