class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        (start_dic, end_dic) = ({}, {})
        m_len_interval = []
        latest = -1
        for (step, position) in enumerate(arr):
            if position - 1 not in end_dic and position + 1 not in start_dic:
                start_dic[position] = 1
                end_dic[position] = 1
                if m == 1:
                    m_len_interval.append((position, position))
            if position - 1 in end_dic and position + 1 not in start_dic:
                length = end_dic[position - 1]
                old_start_index = position - 1 - length + 1
                old_end_index = position - 1
                if length == m:
                    m_len_interval.remove((old_start_index, old_end_index))
                new_start_index = old_start_index
                new_end_index = position
                start_dic[new_start_index] = length + 1
                del end_dic[old_end_index]
                end_dic[new_end_index] = length + 1
                if length + 1 == m:
                    m_len_interval.append((new_start_index, new_end_index))
            if position - 1 not in end_dic and position + 1 in start_dic:
                length = start_dic[position + 1]
                old_start_index = position + 1
                old_end_index = old_start_index + length - 1
                if length == m:
                    m_len_interval.remove((old_start_index, old_end_index))
                new_start_index = position
                new_end_index = old_end_index
                del start_dic[old_start_index]
                start_dic[new_start_index] = length + 1
                end_dic[new_end_index] = length + 1
                if length + 1 == m:
                    m_len_interval.append((new_start_index, new_end_index))
            if position - 1 in end_dic and position + 1 in start_dic:
                old_len_1 = end_dic[position - 1]
                old_start_index_1 = position - 1 - old_len_1 + 1
                old_end_index_1 = position - 1
                if old_len_1 == m:
                    m_len_interval.remove((old_start_index_1, old_end_index_1))
                old_len_2 = start_dic[position + 1]
                old_start_index_2 = position + 1
                old_end_index_2 = position + 1 + old_len_2 - 1
                if old_len_2 == m:
                    m_len_interval.remove((old_start_index_2, old_end_index_2))
                new_start = old_start_index_1
                new_end = old_end_index_2
                new_len = old_len_1 + 1 + old_len_2
                if new_len == m:
                    m_len_interval.append((new_start, new_end))
                start_dic[new_start] = new_len
                end_dic[new_end] = new_len
                del start_dic[old_start_index_2]
                del end_dic[old_end_index_1]
            if m_len_interval:
                latest = step
        return latest + 1 if latest != -1 else -1
