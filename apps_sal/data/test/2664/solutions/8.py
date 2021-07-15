import sys


print("1")
print("3 1 1 2")
print("3 3 3 4")
sys.stdout.flush()
wt=eval(input())

if(wt==0):
	print("2")
	sys.stdout.flush()
	print("5")
	sys.stdout.flush()

elif(wt<0):
	if wt==-1:
		print("2")
		sys.stdout.flush()
		print("4")
		sys.stdout.flush()
	elif wt==-2:
		print("2")
		sys.stdout.flush()
		print("3")
		sys.stdout.flush()

elif(wt>0):
	if wt==1:
		print("2")
		sys.stdout.flush()
		print("2")
		sys.stdout.flush()
	elif wt==2:
		print("2")
		sys.stdout.flush()
		print("1")
		sys.stdout.flush()
