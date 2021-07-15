class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        openedBox = set()
        bfs = [i for i in boxes if status[i]]
        
#BFS every open box
        while bfs:
            size = len(bfs)
            
            for _ in range(size):
                box = bfs.pop(0)
                openedBox.add(box)
#                 Get all boxs in given box, push to queue if it's open
                for eachContainedBox in containedBoxes[box]:
                    if status[eachContainedBox]:
                        bfs.append(eachContainedBox)
                    boxes.add(eachContainedBox)
#                 check all the keys in given box, push box to queue if there is key to the box
                for eachKey in keys[box]:
                    if status[eachKey] == 0 and eachKey in boxes:
                        bfs.append(eachKey)
                    
#                 it's necessary to update status, because above you need use status[eachKey] == 0 to filter out the box that you have alreay taken candies
                    status[eachKey] = 1
                        
        return sum(candies[box] for box in openedBox)
