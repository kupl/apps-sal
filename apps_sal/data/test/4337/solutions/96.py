n = int(input())
a = [s for s in input().split()]

seta = set(a)
if len(seta) == 4: print('Four')
else: print('Three')

