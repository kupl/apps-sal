class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        fruitCap = [0] * len(tree)
        fruitCap[-1] = 1

        fruitA = tree[-1]
        fruitB = None
        for i in reversed(list(range(len(tree) - 1))):
            if tree[i] == fruitA or tree[i] == fruitB:
                fruitCap[i] = fruitCap[i + 1] + 1
            elif fruitB == None:
                fruitCap[i] = fruitCap[i + 1] + 1
                fruitB = tree[i]
            else:
                fruitA = tree[i]
                fruitB = tree[i + 1]
                fruitCap[i] = getConsecutive(tree, i + 1) + 1

        print(fruitCap)
        return max(fruitCap)


def getConsecutive(tree, index):

    consecutive = 0
    fruit = tree[index]
    for i in range(index, len(tree)):
        if tree[i] == fruit:
            consecutive += 1
        else:
            break

    return consecutive
