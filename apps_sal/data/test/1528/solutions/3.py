import sys
sys.setrecursionlimit(10**5)
N, X = map(int, input().split())

layers = [1]
patties = [1]

for i in range(1, N+1):
	layer_i = 2 * layers[i-1] + 3
	patty_i = 2 * patties[i-1] + 1
	layers.append(layer_i)
	patties.append(patty_i)
	
def f(n, x):
	if x == 1:
		return 1 if n == 0 else 0
		
	elif 1 < x <= 1 + layers[n-1]:
		return f(n-1, x-1)
		
	elif x == 2 + layers[n-1]:
		return patties[n-1] + 1
		
	elif 2 + layers[n-1] < x <= 2 + 2 * layers[n-1]:
		return patties[n-1] + 1 + f(n-1, x-2-layers[n-1])
		
	else:
		return 2 * patties[n-1] + 1
		
print(f(N, X))
