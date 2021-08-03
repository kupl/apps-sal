class Solution:
    def find(self, candidates, result, current, target, pos, num, current_num):
        if target == 0:
            temp = current[:]
            result.append(temp)
        else:
            for i in range(pos, len(candidates)):
                n = str(candidates[i])
                if candidates[i] > target or num[n] < current_num[n]:
                    break
                if num[n] == current_num[n]:
                    continue
                current.append(candidates[i])
                current_num[n] += 1
                self.find(candidates, result, current, target - candidates[i], i, num, current_num)
                value = current.pop()
                current_num[str(value)] -= 1

    def combinationSum2(self, candidates, target):
        result = []
        current = []
        candidates.sort()
        can = candidates[:]
        count = 0
        num = {}
        current_num = {}
        for i in range(len(candidates)):
            if i == 0 or candidates[i] != candidates[i - 1]:
                num[str(candidates[i])] = 1
                current_num[str(candidates[i])] = 0
                continue
            else:
                num[str(candidates[i])] += 1
                del can[i - count]
                count += 1
        self.find(can, result, current, target, 0, num, current_num)
        return result
