class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        visited = {}
        arrLen = len(arr)

        def check(i0):
            if i0 in visited:
                return visited[i0]
            di = 1
            preV = 0
            subAns = 1
            while di <= d and i0 + di < arrLen and arr[i0 + di] < arr[i0]:
                if arr[i0 + di] >= preV:
                    subAns = max(subAns, 1 + check(i0 + di))
                preV = max(preV, arr[i0 + di])
                di += 1

            di = 1
            preV = 0
            while di <= d and i0 - di >= 0 and arr[i0 - di] < arr[i0]:
                if arr[i0 - di] >= preV:
                    subAns = max(subAns, 1 + check(i0 - di))
                preV = max(preV, arr[i0 - di])
                di += 1

            visited[i0] = subAns
            return subAns

        ans = 1
        for i in range(arrLen):
            ans = max(ans, check(i))

        # print(visited)

        return ans
