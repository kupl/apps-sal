from sys import stdin,stdout
# stdin = open("/Users/seeva92/Workspace/Contests/1.txt","r")
# stdout = open("/Users/seeva92/Workspace/Contests/2.txt","w")
t,sx,sy,ex,ey = map(int,stdin.readline().split())
def main():
	nonlocal t,sx,sy,ex,ey
	s = stdin.readline()
	if sx == ex and sy == ey: 
		stdout.write("0")
		return
	c = 0
	for i in s:
		c+=1
		if i == 'S' and abs(ey - (sy-1)) < abs(ey - sy):						
			sy-=1
		elif i=='N' and abs(ey - (sy+1)) < abs(ey - sy):			
			sy+=1
		elif i=='E' and abs(ex - (sx+1)) < abs(ex - sx):			
			sx+=1
		elif i=='W' and abs(ex - (sx-1)) < abs(ex - sx):			
			sx-=1
		# print(sx,sy)
		if c>t: break;	
		if sx == ex and sy==ey: break
	if c<=t and sx==ex and sy==ey:
		stdout.write(str(c))
	else: stdout.write("-1")
main()
