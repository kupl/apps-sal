class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        ret=0
        collected_keys=set()
        opened=set()
        queue=initialBoxes
        while queue:
            cont=False
            for i in range(len(queue)):
                box_index=queue.pop(0)
                if status[box_index] or box_index in collected_keys:
                    if box_index not in opened:
                        cont=True
                        opened.add(box_index)
                        ret+=candies[box_index]
                        queue+=containedBoxes[box_index]
                        collected_keys.update(keys[box_index])
                else:
                    queue.append(box_index)
            if not cont: break
        return ret
