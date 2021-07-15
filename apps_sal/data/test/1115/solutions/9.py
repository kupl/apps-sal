N = int(input())
As = list(map(int, input().split()))
sumOfAs = sum(As)
M = int(input())
(maxL, maxR) = 0, 0
isPossible = False
solution = -1
for m in range(M):
	maxL, maxR = list(map(int, input().split()))
	if not isPossible and sumOfAs <= maxR:
		isPossible = True
		solution = max(maxL, sumOfAs)
print(solution)

