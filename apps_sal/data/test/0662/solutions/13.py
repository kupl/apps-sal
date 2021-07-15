l = [int(input()) for _ in range(int(input()))]
p = {1, 2}
for e in l:
	if e in p:
		p = {1, 2, 3} - p | {e}
	else:
		print("NO")
		return
print("YES")

