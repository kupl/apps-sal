class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        seen = set(A)
        sequence_lens = []
        
        for i in range(len(A)):
            prev_num = A[i]
            for j in range(i + 1, len(A)):
                
                curr_num = A[j]
                seq_len = 2
                #li = [prev_num, curr_num]
                while prev_num + curr_num in seen:
                    #print(f'{prev_num} + {curr_num} = {prev_num + curr_num}')
                    seq_len += 1
                    next_num = prev_num + curr_num
                    prev_num = curr_num
                    curr_num = next_num
                    #i.append(next_num)
                prev_num = A[i]
                if seq_len > 2:
                    #print(li)
                    sequence_lens.append(seq_len)
        return max(sequence_lens) if len(sequence_lens) > 0 else 0
