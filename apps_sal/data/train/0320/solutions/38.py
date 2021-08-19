

def val(n):
    c = 0
    while(n > 1):
        if n % 2 == 1:
            c += 1
            n -= 1
        else:
            n = n // 2
            # c += 1
    return c


def ma(n):
    c = 0
    while(n > 1):
        if n % 2 == 1:
            # c +=1
            n -= 1
        else:
            n = n // 2
            c += 1
    return c


class Solution:
    def minOperations(self, n: List[int]) -> int:
        c = ma(max(n))

        for i in range(len(n)):
            if n[i] > 0:
                c += val(n[i]) + 1

        return c
