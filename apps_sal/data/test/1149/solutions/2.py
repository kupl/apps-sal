n = int(input())
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]

if set(a1[1:]) | set(a2[1:])  == set(range(1,n+1)):
	print('I become the guy.')
else:
	print('Oh, my keyboard!')
