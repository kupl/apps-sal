class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        mod_gap = sum(digits) % 3
        if mod_gap == 0:
            answer = ''.join([str(i) for i in sorted(digits, reverse=True)])
        mult3 = [i for i in digits if i % 3==0]
        non3 = [i for i in digits if i % 3!=0]
        non3 = sorted(non3, reverse=True)

        if mod_gap == 1:
            last_odd_idx = [i for i in range(len(non3)) if non3[i] & 1]
            if len(last_odd_idx) > 0:
                last_odd_idx = last_odd_idx[-1]
                non3 = non3[:last_odd_idx] + non3[last_odd_idx+1:]
        elif mod_gap==2:
            last_even_idx =  [i for i in range(len(non3)) if non3[i] % 2==0]
            if len(last_even_idx) > 0:
                last_even_idx = last_even_idx[-1]
                non3 = non3[:last_even_idx] + non3[last_even_idx+1:]
            
        if sum(non3) % 3 != 0:
            non3 = []
        answer = ''.join([str(int(i)) for i in sorted(mult3+non3, reverse=True)])
        
        
        while answer.startswith('0') and len(answer)>1:
            answer = answer[1:] 
        return answer
            

