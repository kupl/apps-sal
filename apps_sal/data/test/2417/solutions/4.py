n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l1.reverse()
l2.reverse()
trans = [0] * n
for i in range(n):
	trans[l1[i] - 1] = i
end = [0] * n
for i in range(n):
	end[i] = trans[l2[i] - 1]
wyn = 0
maksi = end[0]
for i in range(1, n):
	if end[i] < maksi:
		wyn += 1
	maksi = max(end[i], maksi)
print(wyn)
