class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        self.groups_start = {}
        self.groups_end = {}
        last_pos = -1
        m_start_pos = set()
        n = len(arr)
        for (k, i) in enumerate(arr):
            start_pos = i
            if i + 1 <= n:
                if i + 1 in self.groups_start:
                    length = self.groups_start[i + 1]
                    del self.groups_start[i + 1]
                    self.groups_start[i] = length + 1
                    self.groups_end[i + length] = i
                    if i + 1 in m_start_pos:
                        m_start_pos.remove(i + 1)
                else:
                    self.groups_start[i] = 1
                    self.groups_end[i] = i
            else:
                self.groups_start[i] = 1
                self.groups_end[i] = i
            if i - 1 >= 1:
                if i - 1 in self.groups_end:
                    start_pos = self.groups_end[i - 1]
                    if start_pos in m_start_pos:
                        m_start_pos.remove(start_pos)
                    new_length = self.groups_start[start_pos] + self.groups_start[i]
                    self.del_group(i)
                    self.del_group(start_pos)
                    self.groups_start[start_pos] = new_length
                    self.groups_end[start_pos + new_length - 1] = start_pos
            if self.groups_start[start_pos] == m:
                m_start_pos.add(start_pos)
            if len(m_start_pos) > 0:
                last_pos = k + 1
        return last_pos

    def del_group(self, start_pos):
        del self.groups_end[start_pos + self.groups_start[start_pos] - 1]
        del self.groups_start[start_pos]
