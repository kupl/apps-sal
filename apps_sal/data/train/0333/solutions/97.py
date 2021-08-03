class Solution:
    def minJumps(self, arr: List[int]) -> int:
        x = []
        x.append(arr[0])
        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i - 1] and arr[i] == arr[i + 1]:
                continue
            else:
                x.append(arr[i])
        if len(arr) > 1:
            x.append(arr[-1])
        arr = x
        d = collections.defaultdict(list)
        for i in range(len(arr)):
            d[arr[i]].append(i)
        bfs = [0]
        steps = 0
        temp = []
        seen = set([0])
        while len(bfs) > 0:
            index = bfs.pop()
            if index == len(arr) - 1:
                return steps
            if (index + 1) < len(arr) and (index + 1) not in seen:
                temp.append(index + 1)
                seen.add(index + 1)
            if (index - 1) >= 0 and (index - 1) not in seen:
                temp.append(index - 1)
                seen.add(index - 1)
            for i in d[arr[index]]:
                if i not in seen:
                    temp.append(i)
                    seen.add(i)

            if len(bfs) == 0:
                bfs = temp
                temp = []
                steps += 1

        return steps
