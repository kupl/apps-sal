def get_tuple():
	a, A = list(map(int, input().split()))
	b, B = list(map(int, input().split()))
	return (a,B), (b,A)

def larger(a1, a2):
	return a1[0] > a2[1] and a1[1] > a2[0]

def smaller(a1, a2):
	return a1[0] < a2[1] and a1[1] < a2[0]

t11, t12 = get_tuple()
t21, t22 = get_tuple()

if larger(t11,t21) and larger(t11, t22):
	print("Team 1")
elif larger(t12, t21) and larger(t12, t22):
	print("Team 1")
elif (smaller(t11,t21) or smaller(t11, t22)) and (smaller(t12, t21) or smaller(t12, t22)):
	print("Team 2")
else:
	print("Draw")




