import sys
input=sys.stdin.readline
import math
# sys.setrecursionlimit(10**9)
def construct(array,cur_pos,tree,start,end):
	if(start==end):
		# print(cur_pos,"pppp",array[start])
		tree[cur_pos]=array[start]

	else:
		mid=(start+end)//2
		w=(n1-int(math.log2(cur_pos+1)))
		# print(w,n1,cur_pos+1)
		if(w%2!=0):
			# print(cur_pos,w)
			tree[cur_pos]=(construct(array,2*cur_pos+1,tree,start,mid)|construct(array,2*cur_pos+2,tree,mid+1,end))
		else:

			# print(cur_pos,w)
			tree[cur_pos]=(construct(array,2*cur_pos+1,tree,start,mid)^construct(array,2*cur_pos+2,tree,mid+1,end))
		
			
		
	return tree[cur_pos]

def update(cur_pos,l,r,index,increment):
	# print(tree)
	if(l<=index<=r):
		if(l==r):
			tree[cur_pos]=increment
		else:
			mid=(l+r)//2
			w=(n1-int(math.log2(cur_pos+1)))
			if(w%2!=0):
				update(2*cur_pos+1,l,mid,index,increment)
				update(2*cur_pos+2,mid+1,r,index,increment)
				tree[cur_pos]=tree[2*cur_pos+1]|tree[2*cur_pos+2]
			else:
				update(2*cur_pos+1,l,mid,index,increment)
				update(2*cur_pos+2,mid+1,r,index,increment)
				tree[cur_pos]=tree[2*cur_pos+1]^tree[2*cur_pos+2]
		return tree[cur_pos]
	return 0


l= list(map(int,input().split())) 
l1=list(map(int,input().split())) 
n=(2**(l[0]))
tree=[0]*(2**(l[0]+1)-1)
n1=int(math.log2(len(tree)))
# print(n1,n,"llll")
construct(l1,0,tree,0,n-1)
# print(tree)
for i in range(l[1]):
	# print(tree)
	l2=list(map(int,input().split())) 
	

	update(0,0,n-1,l2[0]-1,l2[1])
	# print(tree,"ppp")
	print(tree[0])




