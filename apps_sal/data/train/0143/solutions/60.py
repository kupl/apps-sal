class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if(len(tree) <= 1):
            return len(tree)
        if(len(list(set(tree))) == 2):
            return len(tree)
        maxCount = 0
        classes = []
        i = 0
        while(i < len(tree)):
            j = i + 1
            classes = [tree[i]]
            count = 1
            secFruitStart = -1
            while(len(classes) <= 2 and j < len(tree)):
                if(tree[j] not in classes):
                    classes.append(tree[j])
                    if(len(classes) == 2):
                        secFruitStart = j
                if(len(classes) == 3):
                    continue
                count = count + 1
                j = j + 1
            if(count > maxCount):
                maxCount = count
            if(secFruitStart != -1):
                i = secFruitStart
            else:
                break
        return maxCount
