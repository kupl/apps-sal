class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        records = []
        self.num_m = 0
        for i in range(len(arr)):
            records.append([-1, 0])

        def find(i):
            if records[i][0] == -1:
                return -1
            elif records[i][0] == i:
                return i
            else:
                ii = find(records[i][0])
                records[i][0] = ii
                return ii

        def union(i, j):
            ans_i = find(i)
            ans_j = find(j)
            if records[ans_i][1] > records[ans_j][1]:
                records[ans_j][0] = ans_i
                if m == records[ans_i][1]:
                    self.num_m -= 1
                if m == records[ans_j][1]:
                    self.num_m -= 1
                records[ans_i][1] += records[ans_j][1]
                if m == records[ans_i][1]:
                    self.num_m += 1
            else:
                records[ans_i][0] = ans_j
                if m == records[ans_i][1]:
                    self.num_m -= 1
                if m == records[ans_j][1]:
                    self.num_m -= 1
                records[ans_j][1] += records[ans_i][1]
                if m == records[ans_j][1]:
                    self.num_m += 1
        last = -1
        for (i, n) in enumerate(arr):
            num = n - 1
            records[num] = [num, 1]
            if m == 1:
                self.num_m += 1
            if num >= 1 and records[num - 1][0] != -1:
                if records[num - 1][1] == 1:
                    union(num - 1, num)
                else:
                    union(num - 1, num)
            if num < len(arr) - 1 and records[num + 1][0] != -1:
                if records[num + 1][1] == 1:
                    union(num + 1, num)
                else:
                    union(num + 1, num)
            if self.num_m > 0:
                last = i + 1
        return last
