n = int(input().strip())
temp = input().strip().split()
w = []
for j in range(len(temp)):
	w.append([int(temp[j]),j])

w.sort()
#print(w)
passenger = input().strip()

biggest_intro = []
smallest_index = 0

for i in range(2*n):
	if passenger[i] == '0':
		#introvert
		#smallest_empty = w[smallest_index][1]		#actual index
		print(w[smallest_index][1]+1, end=' ')
		biggest_intro.append(smallest_index)		#non-actual index, bigger width at the end
		smallest_index+=1
	elif passenger[i] == '1':
		b = biggest_intro.pop()
		print(w[b][1]+1,end=' ')

	#print(biggest_intro)
print()

