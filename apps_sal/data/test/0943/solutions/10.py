n = int(input())
N = [int(x) for x in input().split()]
S = sum(N)
odd = [x for x in N if x % 2 == 1]
x = min(odd) if len(odd) > 0 else 0
print(S - x if S % 2 else S)
