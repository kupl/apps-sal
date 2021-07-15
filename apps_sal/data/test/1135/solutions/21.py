a = int(input())
s = input()
ans = ""
if (a%2 == 0) : cnt = 0
else : cnt = 1
for i in s:
	cnt += 1
	if (cnt%2 == 1) : ans = i+ans
	else : ans = ans+i
	#print(ans)
print(ans)
