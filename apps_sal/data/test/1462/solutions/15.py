count = [0]*26
n, k = list(map(int , input().split()))
cards = input()
for c in cards:
	count[ord(c)-ord('A')]+=1

count.sort(reverse=True)
ans = 0
for c in count:
	if (k - c) >= 0:
		ans += c**2
		k-=c
	else:
		ans += k**2
		break

print(ans)

