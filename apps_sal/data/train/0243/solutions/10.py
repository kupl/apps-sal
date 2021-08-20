class Solution:

    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        front = dict()
        back = dict()
        for i in range(len(fronts)):
            if fronts[i] in front:
                front[fronts[i]].add(i)
            else:
                front[fronts[i]] = {i}
            if backs[i] in back:
                back[backs[i]].add(i)
            else:
                back[backs[i]] = {i}
        ans = float('inf')
        aux = set()
        for elem in front:
            if elem not in aux:
                if elem not in back:
                    ans = min(ans, elem)
                else:
                    flag = 1
                    for index in back[elem]:
                        if fronts[index] == elem:
                            flag = 0
                    if flag:
                        ans = min(ans, elem)
                aux.add(elem)
        for elem in back:
            if elem not in aux:
                if elem not in front:
                    ans = min(ans, elem)
                else:
                    flag = 1
                    for index in front[elem]:
                        if backs[index] == elem:
                            flag = 0
                    if flag:
                        ans = min(ans, elem)
                aux.add(elem)
        return ans if ans != float('inf') else 0
