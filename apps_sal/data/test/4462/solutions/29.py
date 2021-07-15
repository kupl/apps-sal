n = int(input())
a = list(map(int,input().split()))
t = [0 for _ in range(3)]

for i in range(n):
	if a[i] % 2 == 0:
		if a[i] % 4 == 0:
			t[2] += 1
		else:
			t[1] += 1
	else:
		t[0] += 1

if t[0] + (t[1]%2) <= t[2] + 1:
	print("Yes")
else:
	print("No")
