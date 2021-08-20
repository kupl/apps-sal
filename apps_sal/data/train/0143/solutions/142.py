class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        ans = 0
        past = []
        last = []
        for i in range(len(tree)):
            if len(past) == 0:
                past.append(tree[i])
                last.append(i)
                ans = max(i - last[0] + 1, ans)
                continue
            if len(past) == 1:
                if tree[i] not in past:
                    past.append(tree[i])
                    last.append(i)
                ans = max(i - last[0] + 1, ans)
                continue
            if tree[i] not in past:
                bt = i - 1
                ele = tree[bt]
                while tree[bt] == ele:
                    bt -= 1
                bt += 1
                past = [tree[bt], tree[i]]
                last = [bt, i]
            ans = max(i - last[0] + 1, ans)
        return ans
