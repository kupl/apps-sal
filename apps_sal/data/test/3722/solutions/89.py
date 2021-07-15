import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return list(map(int, input().split()))
sys.setrecursionlimit(10**9)

N = int(input())
AA = input()
AB = input()
BA = input()
BB = input()
mod = 10**9+7

if N<=3:
    print((1))
elif AA=='A' and AB=='A':
    print((1))
elif BB=='B' and AB=='B':
    print((1))
elif (AA, AB, BA, BB) in [("A", "B", "A", "A"),  ("B", "A", "B", "A"), ("B", "A", "B", "B"), ("B", "B", "A", "A")]:
    print((pow(2, N-3, mod)))
else:
    dp = [[0]*2 for _ in range(N)]
    dp[0][0] = 1
    for i in range(1, N):
        # Bが連続しないように置く
        dp[i][0] = (dp[i-1][0] + dp[i-1][1])%mod
        dp[i][1] = dp[i-1][0]%mod
    print((dp[-1][1]))
    

# def f(aa, ab, ba, bb):
#     l = [aa, ab, ba, bb]
#     start = 'AB'
#     se = set([start])
#     while True:
#         new = set()
#         for s in se:
#             lens = len(s)
#             for i in range(lens-1):
#                 new.add(s[:i+1]+l[lis.index(s[i:i+2])]+s[i+1:])
#         if len(s)+1==N:
#             return new
#         se = new

# N = 10
# lis = ['AA', 'AB', 'BA', 'BB']
# for AA in ('A', 'B'):
#     for AB in ('A', 'B'):
#         for BA in ('A', 'B'):
#             for BB in ('A', 'B'):
#                 print(AA, AB, BA, BB, len(f(AA, AB, BA, BB)))

