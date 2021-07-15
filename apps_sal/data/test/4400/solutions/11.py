S = str(input())
ans = 0
if S[0] == "R":
	ans += 1
	if S[1] == "R":
		ans += 1
		if S[2] == "R":
			ans += 1
elif S[0] != "R" and S[1] == "R":
	ans +=1
	if S[2] == "R":
		ans += 1
elif S[0] != "R" and S[1] != "R" and S[2] == "R":
	ans += 1
elif S[0] == S[1] == S[2] != "R":
	ans = 0

print(ans)
