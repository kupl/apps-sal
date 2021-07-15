class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # for initial boxes:
        # - accumulate candies
        # - for each key, pre-unlock them
        # - add containedBoxes to queue
        #
        # for all contained boxes that's open:
        # - accumulate candies
        # - for each key, pre-unlock them
        # ...
        #
        # keep track of a list of opened boxes to explore, and a list of closed boxes to explore
        # - whenever open a box, pre-unlock their keys
        #   - if box in list of closed Q, move to open
        # - whenever find an enclosed box, put to either open or closed
        # - continue until we have no more open boxes
        
        open_boxes = set()
        closed_boxes = set()
        # TODO: may need an explored flag for each box
        for b in initialBoxes:
            if status[b]:
                open_boxes.add(b)
            else:
                closed_boxes.add(b)
        
        total_candies = 0
        while len(open_boxes) > 0:
            b = open_boxes.pop()
            
            total_candies += candies[b]
            
            for key in keys[b]:
                status[key] = 1
                if key in closed_boxes:
                    closed_boxes.remove(key)
                    open_boxes.add(key)
            
            for bb in containedBoxes[b]:
                if status[bb]:
                    open_boxes.add(bb)
                else:
                    closed_boxes.add(bb)
        
        return total_candies
