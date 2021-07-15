#!/usr/bin/env python

def binarySearch(ok, ng, test):
    """ 
    Binary search

    Args:
        ok(int) : test(x) == True を確実に満たす点
        ng(int) : test(x) == False を確実に満たす点
        test(function) : テスト対象の関数
    Returns:
        ok(int) : test(x) == True を確実に満たす点で、
        　　　　　最終的に求まるもの。
    Note:
        https://www.forcia.com/blog/001434.html

    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid):
            ok = mid 
        else:
            ng = mid 
    return ok

def test(x):
    return x*(x+1)//2 <= n+1 

n = int(input())
k = binarySearch(1, 10**18+10, test)
ans = n-k+1
print(ans)

