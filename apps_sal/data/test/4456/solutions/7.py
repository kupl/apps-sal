n, k = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
d = {}
j = 1
for i in l1:
    d[i] = j
    j += 1
l = [d[i] for i in l2]
#l is the list that forces shit
wei = [0] * (n+2)
right = [0] * (n+2)
for i in range(n -1):
    #look at l[i], l[1+1]
    if l[i] < l[i+1]:
        continue
    wei[l[i+1]] += 1
    wei[l[i] + 1] -= 1
    right[l[i]] += 1
odcinki = []
l = 1
r = 1
pref = [0] * (n + 2)
for i in range(1, n+2):
    pref[i] = pref[i-1] + wei[i]
for i in range(1, n + 2):
    if pref[i] == 0:
        odcinki.append([l,r])
        l = i + 1
        r = i + 1
    else:
        if pref[i] == right[i]:
            odcinki.append([l,r])
            l = i + 1
            r = i + 1
 
        else:
            r += 1
if odcinki[0] == [1,1]:
	odcinki = odcinki[1:]
if odcinki[-1][0] == odcinki[-1][1] and odcinki[-1][0] > n:
	odcinki = odcinki[:-1]
 
lewe = [0] * (n+1)
prawe = [0] * (n+1)
for i in odcinki:
	lewe[i[0]] = 1
	prawe[i[1]] = 1
odp = [0] * (n+3)
i = -1
indx = 1
reg = 0
odp = [-1] * (n+3)
count = 0
while indx < n + 1:
	#i stays the same iff [5,6,7,8,9] we are 6,7,8,9
	if prawe[indx-1] == 1:
		reg = 0
	if lewe[indx] == 1:
		reg = 1
		count = 0
	odp[indx] = i
	#kiedy i += 1
	if count == 0 or reg == 0:
		i += 1
	count += 1
	odp[indx] = i
	indx += 1
odpp = [0] * (n + 3)
for i in range(n):
    odpp[l1[i]] = odp[i + 1]
odpp = odpp[1:-2]
if max(odpp) + 1 < k:
	print("NO")
else:
	print("YES")
	for i in range(n):
		print(chr(97+min(25, odpp[i])), end = "")
