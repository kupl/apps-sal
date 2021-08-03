class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        l = len(arr)
        x = [[] for x in range(l + 1)]
        if l == m:
            return l

        last = -1
        lens = [0 for x in range(l + 1)]
        for i in range(0, l):
            cur = arr[i]
            right = []
            left = []
            if cur + 1 < l + 1:
                right = x[cur + 1]
            if cur - 1 >= 0:
                left = x[cur - 1]

            lv = rv = cur
            ss = 1
            if left:
                lv = left[1]
                ss += left[0]
                lens[left[0]] -= 1
                if left[0] == m:
                    last = i
            if right:
                rv = right[2]
                ss += right[0]
                lens[right[0]] -= 1
                if right[0] == m:
                    last = i
            lens[ss] += 1
            x[lv] = [ss, lv, rv]
            x[rv] = [ss, lv, rv]

        return last

        for i in range(l - 1, 0, -1):
            cur = arr[i]
            if lC[cur] or rC[cur]:
                return i
            if cur + m + 1 <= l:
                temp = True
                for j in range(cur + 1, cur + m + 1):
                    if rC[j]:
                        rC[j] = False
                        temp = False
                        break
                if temp:
                    rC[cur + m + 1] = True
            if cur - m - 1 >= 0:
                temp = True
                for j in range(cur - m, cur):
                    if lC[j]:
                        lC[j] = False
                        temp = False
                        break
                if temp:
                    lC[cur - m - 1] = True
        return -1

        mx = l
        mxcount = 1
        ls = [l]
        for i in range(l - 1, -1, -1):
            cur = arr[i]
            prev = 0
            j = self.bisearch(cur, done, 0, len(done))
            val = done[j]
            prev = done[j - 1]

            if m == val - cur - 1 or m == cur - prev - 1:
                return i

            done = done[:j] + [cur] + done[j:]

        return -1

    def bisearch(self, cur: List[int], arr: List[int], i: int, j: int) -> int:
        if i == j:
            return j
        if j - i <= 1:
            if arr[i] < cur:
                return j
            else:
                return i
        mid = (j - i) // 2
        if cur < arr[i + mid]:
            return self.bisearch(cur, arr, i, i + mid)
        else:
            return self.bisearch(cur, arr, i + mid, j)
