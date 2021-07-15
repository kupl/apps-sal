n=int(input())
a=[int(i) for i in input().split()]
s,f=(int(i) for i in input().split())
pref=[a[0]]
for i in range(1,n):
	pref.append(a[i]+pref[i-1])
	
def nb_people(strt, end):
	if strt<=end:
		if strt==0:
			return pref[end]
		else:
			return pref[end]-pref[strt-1]
	else:
		ret = pref[end]+pref[n-1]
		if strt>0:
			ret-=pref[strt-1]
		return ret
	
max_people=0
opt_h=0
for h in range(1,n+1):
	strt=s-h+1#à h heures ds le 1er fuseau où est - il s heures ?
	if strt<=0:
		strt+=n
	end =f-h#pareil avec f-1
	if end<=0:
		end+=n
	tmp_people = nb_people(strt-1, end-1)
	#print("h",h,"strt", strt, "end", end,"tmp_people",tmp_people)
	if tmp_people>max_people:
		max_people=tmp_people
		opt_h = h
print(opt_h)

