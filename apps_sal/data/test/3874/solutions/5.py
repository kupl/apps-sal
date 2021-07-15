num_files, num_delete = list(map(int, input().split(' ')))

files = []
while num_files > 0:
	files.append( input() )
	num_files -= 1

indices_del = list( [x - 1 for x in list(map(int, input().split(' ')))] )
ind = 0

to_del = []
to_leave = []
for i in indices_del:
	if len(to_del) > 0 and len(files[i]) != len(to_del[0]):
		print ('No')
		return
	to_del.append(files[i])

for i in range(len(files)):
	if ind < len(indices_del) and i == indices_del[ind]:
		ind += 1
		continue
	if len(files[i]) == len(to_del[0]):
		to_leave.append(files[i])
	
res = []	
for pos in range(len(to_del[0])):
	d = set()
	for del_file in to_del:
		ch = del_file[pos]
		d.add( ch )
	if len(d) > 1:
		res.append( '?' )
	else:
		undef = False
		for leave_file in to_leave:
			pass
			'''
			if leave_file[pos] == ch:
				res.append( '?' )
				undef = True
			'''
		if not undef:
			res.append( ch )
			fn = lambda f: f[pos] == ch
			to_leave = list( filter(fn, to_leave) )

if len(to_leave) > 0:
	print('No')
else:
	print ('Yes')
	print(''.join(res))
			



