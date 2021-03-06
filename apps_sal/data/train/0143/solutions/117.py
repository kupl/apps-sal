class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        fruit_dict = collections.defaultdict(int)
        (j, result, count) = (0, 0, 0)
        for (i, t) in enumerate(tree):
            fruit_dict[t] += 1
            count += 1
            while len(fruit_dict) > 2 and j < len(tree):
                fruit_dict[tree[j]] -= 1
                count -= 1
                if fruit_dict[tree[j]] == 0:
                    del fruit_dict[tree[j]]
                j += 1
            if len(fruit_dict) <= 2:
                result = max(result, count)
        return result
        '\n        blocks = [(k,len(list(v))) for k,v in itertools.groupby(tree)]\n        i,result=0,0\n        \n        while i<len(blocks):\n            j=i\n            count=0\n            fruit_set = set()\n            while j<len(blocks):\n                fruit_set.add(blocks[j][0])\n                count+=blocks[j][1]\n                if len(fruit_set)>2:\n                    i=j-1\n                    break\n                result=max(result,count)\n                j+=1\n            else:\n                break\n            \n        return result\n        '
