n, c = map(int, input().split())
P = list(map(int, input().split()))
T = list(map(int, input().split()))
t = 0
L = 0
for i in range(n):
	t += T[i]
	L += max(P[i] - c * t, 0)
t = 0
R = 0
for i in range(n - 1, -1, -1):
	t += T[i]
	R += max(P[i] - c * t, 0)
if L > R:
	print("Limak")
elif R > L:
	print("Radewoosh")
else:
	print("Tie")
