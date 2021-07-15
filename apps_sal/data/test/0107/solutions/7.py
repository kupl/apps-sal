# Main maut ko takiya, aur kafan ko chaadar banakar audhta hoon!

s=input()

d=s.find('1')

if d!=-1 and s[d+1:].count('0')>=6:
	print("yes")
else:
	print("no")
