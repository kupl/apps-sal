N=int(input())
def rec(n):
    if n < 0: return False
    if n % 4 == 0 or n % 7 == 0: return True
    else: return rec(n-4)
if rec(N): print('Yes')
else: print('No')
