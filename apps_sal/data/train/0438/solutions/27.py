class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        start_dict = {}
        end_dict = {}
        m_dict = {}
        last_step = -2
        for i, num in enumerate(arr):
            if num + 1 not in start_dict and num - 1 not in end_dict:
                start = num
                end = num
            if num + 1 in start_dict and num-1 not in end_dict:
                end = start_dict.pop(num+1)
                start = num
                m_dict[end - num].remove(num+1)
            if num + 1 not in start_dict and num - 1 in end_dict:
                start = end_dict.pop(num-1)
                end = num
                m_dict[num-start].remove(start)
            if num + 1 in start_dict and num - 1 in end_dict:
                end = start_dict.pop(num+1)
                start = end_dict.pop(num-1)
                m_dict[end-num].remove(num+1)
                m_dict[num-start].remove(start)
            start_dict[start] = end
            end_dict[end] = start
            m_dict.setdefault(end - start + 1, set()).add(start)
            if m in m_dict and m_dict[m]:
                last_step = i
        return last_step+1

