# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
even = list([x for x in A if x % 2 == 0])
odd = list([x for x in A if x % 2 != 0])
even = sorted(even)
odd = sorted(odd)

evenN = len(even)
oddN = len(odd)

ans = -1
if abs(evenN - oddN) <= 1:
    ans = 0
else:
    if evenN > oddN:
        ans = sum(even[:evenN - oddN - 1])
    else:
        ans = sum(odd[:oddN - evenN - 1])
print(ans)
