from heapq import merge
def f(s):
    l = len(s)
    return [list(merge(f(s[:l>>1]),f(s[l>>1:])))] if l & 1 == 0 else [s] 
print('YES' if f(input()) == f(input()) else 'NO')

