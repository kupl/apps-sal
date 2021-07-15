n = int(input())
a = list(map(int,input().split()))
targ = 0
for j in a:
	targ += 1/j
print(1/targ)
