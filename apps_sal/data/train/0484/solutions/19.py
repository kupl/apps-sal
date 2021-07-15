class Solution:
    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2

        N_ary = []
        compute_N = N
        while not compute_N == 0:
            N_ary.insert(0, compute_N % 10)
            compute_N //= 10
            
        middle = len(N_ary) // 2
        for i in range(middle, len(N_ary)):
            N_ary[i] = N_ary[len(N_ary) - 1 - i] = min(N_ary[i], N_ary[len(N_ary) - 1 - i])
            
        result = 0
        while True:
            num = self.ary_to_int(N_ary)
            if num < N:
                N_ary = self.compute_next_ary(N_ary)
                continue
            is_prime = True
            for i in range(2, num):
                if i**2 > num:
                    break
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                result = num
                break
            N_ary = self.compute_next_ary(N_ary)
            
        return result


    def ary_to_int(self, ary: List[int]) -> int:
        result = 0
        for num in ary:
            result = result * 10 + num
        return result
    
        
    def compute_next_ary(self, ary: List[int]) -> List[int]:
        middle = len(ary) // 2

        is_all_nine = True
        for i in range(middle, len(ary)):
            if not ary[i] == 9:
                is_all_nine = False
                break                
        if is_all_nine:
            ary = [0 for i in range(len(ary) + 1)]
            ary[0] = ary[-1] = 1
            return ary
        
        for i in range(middle, len(ary)):
            if ary[i] == 9:
                ary[i] = ary[len(ary) - 1 - i] = 0
            else:
                ary[i] = ary[len(ary) - 1 - i] = ary[i] + 1
                break
        return ary

