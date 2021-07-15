class Solution:
    def consecSumIncludeA(self, N: int, A: int) -> List[int]:
        csum = A
        c = A
        while csum < N:
            c += 1
            csum += c
        if csum == N:
            return 1
        return 0
    
    def consecutiveNumbersSumtimeout(self, N: int) -> int:
        if N == 1:
            return 1
        uplim = int(N/2)
        if N%2==1:
            uplim = int((N//2)+1)
        fin = 1
        for ii in range(1,uplim+1):
            # print(\"ii now: {}; fin now: {}\".format(ii,fin))
            fin += self.consecSumIncludeA(N-ii,ii+1)
        return fin
    
    def consecutiveNumbersSum(self, N: int) -> int:
        # if N = sum([1,...,x])+x.a, then N can be expressed as a sum of x consecutive numbers
        if N == 1:
            return 1
        combo = 1 
        fin = 1
        form = 2
        sumsf = 1
        while form < 2*N:
            # print(\"form: {}, fin: {}\".format(form, fin))
            combo += 1
            if (N-sumsf)%combo == 0:
                fin += 1
            form = combo+combo**2
            sumsf += combo
        return fin

