n = int(input())
a = [int(i) for i in input().split()]
once = 0
twice = 2**64
for i in a:
    twice |= (once & i)
    once |= i
a = sorted([(i & ~twice,i) for i in a],reverse=True)
a = [j for i,j in a]
print(*a)

