class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        '''
        f(n) = 1/n                                    -> 1st person picks his own seat
            + 1/n * 0                                 -> 1st person picks last one's seat
            + (n-2)/n * (                            ->1st person picks one of seat from 2nd to (n-1)th
                1/(n-2) * f(n-1)                   -> 1st person pick 2nd's seat
                1/(n-2) * f(n-2)                  -> 1st person pick 3rd's seat
                ......
                1/(n-2) * f(2)                     -> 1st person pick (n-1)th's seat
            )

        => f(n) = 1/n * ( f(n-1) + f(n-2) + f(n-3) + ... + f(1) )
        '''
        if n == 1:
            return 1.0
        if n == 2:
            return 0.5
        dp = [1.0, 0.5]
        acc = 1.5
        for i in range(3, n + 1):
            dp.append(acc / i)
            acc += dp[-1]
        return dp[-1]

        '''
        Formal proof with math solution
        when n > 2,
        f(n) = 1/n * ( f(n-1) + f(n-2) + ... + f(1) )
        f(n-1) = 1/(n-1) * (f(n-2) + f(n-3) + ... + f(1))

        because, the 2nd equation requires n-1 > 1
        So that

        n * f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1)
        (n-1) * f(n-1) = f(n-2) + f(n-3) + ... + f(1)
        Substract both sides, we get

        n * f(n) - (n-1)*f(n-1) = f(n-1)

        => n * f(n) = n * f(n-1)
        => f(n) = f(n-1) = f(2) = 1/2 , when n > 2
        '''
