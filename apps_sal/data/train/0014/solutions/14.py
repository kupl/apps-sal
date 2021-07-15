from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return list(map(int, input().split()))
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a1, b1 = iis()	
	a2, b2 = iis()
	if (a1 == a2 and b1+b2 == a1) or (a1 == b2 and a2+b1 == a1) or (a2 == b1 and a1+b2 == a2) or (b2 == b1 and a1+a2 == b2):
		print("Yes")
	else:
		print("No")

