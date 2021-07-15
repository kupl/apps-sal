import sys
f=sys.stdin
out=sys.stdout

q=int(f.readline().rstrip('\r\n'))
pos,id=f.readline().rstrip('\r\n').split()
mid=int(id)

left=[]
right=[]
dleft={}
dright={}

for i in range(q-1):
	pos,id=f.readline().rstrip('\r\n').split()
	id=int(id)
	if pos=="L":
		left.append(id)
		dleft[id]=len(dleft)+1
	elif pos=="R":
		right.append(id)
		dright[id]=len(dright)+1
	else:
		if id==mid:
			out.write(str(min(len(dleft),len(dright)))+"\n")
		elif id in dleft:
			z=len(dleft)-dleft[id]+1
			out.write(str(min(z-1,1+len(dright)+dleft[id]-1))+"\n")
		else:
			z=dright[id]
			#print(z)
			out.write(str(min(len(dleft)+z,len(dright)-z))+"\n")
