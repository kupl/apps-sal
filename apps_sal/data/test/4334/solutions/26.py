D = {}
s, t = input().split()
a, b = map(int, input().split())
D[s] = a
D[t] = b
D[input()] -= 1
print(D[s], D[t]) 
