# import random

# arr1=[random.randint(1,100) for i in range(10)]
# arr2=[random.randint(1,100) for i in range(10)]

# print(arr1,"			SORTED:-",sorted(arr1))
# print(arr2,"			SORTED:-",sorted(arr2))


# def brute_inv(a1,a2):
# 	a3=a1+a2
# 	inv=0
# 	for i in range(len(a3)):
# 		for j in range(i+1,len(a3)):
# 			if a3[i]>a3[j]:
# 				inv+=1
# 	return inv

# def smart_inv(arr1,arr2):
# 	i1,i2=0,0
# 	inv1=0;
# 	while i1<len(arr1) and i2<len(arr2):
# 		if arr1[i1]>arr2[i2]:
# 			inv1+=(len(arr1)-i1)
# 			i2+=1
# 		else:
# 			i1+=1
# 	return inv1

# print(arr1+arr2,smart_inv(sorted(arr1),sorted(arr2)))
# print(brute_inv(arr1,arr2))
# print(arr2+arr1,smart_inv(sorted(arr2),sorted(arr1)))
# print(brute_inv(arr2,arr1))

# if (smart_inv(sorted(arr1),sorted(arr2))<smart_inv(sorted(arr2),sorted(arr1)) and brute_inv(arr1,arr2)<brute_inv(arr2,arr1)) or (smart_inv(sorted(arr2),sorted(arr1))<smart_inv(sorted(arr1),sorted(arr2)) and brute_inv(arr2,arr1)<brute_inv(arr1,arr2)):
# 	print("True")
# else:
# 	print("False")


# print(brute_inv([1,2,10],[3,5,7]))
# print(brute_inv([3,5,7],[1,2,10]))
# print(brute_inv([1,7,10],[3,5,17]))
# print(brute_inv([3,5,17],[1,7,10]))

# 1		:-	1
# 2		:-	10
# 3		:-	011
# 4		:-	0100
# 5		:-	00101
# 6		:-	000110
# 7		:-	0000111
# 8		:-	00001000
# 9		:-	000001001
# 10		:-	0000001010
# 11		:-	00000001011
# 12		:-	000000001100
# 13		:-	0000000001101
# 14		:-	00000000001110
# 15		:-	000000000001111
# 16		:-	0000000000010000


from sys import stdin, stdout

n, m = stdin.readline().strip().split(' ')
n, m = int(n), int(m)
adj = [[] for i in range(n + 1)]

for i in range(m):
    u, v = stdin.readline().strip().split(' ')
    u, v = int(u), int(v)
    adj[u].append((v, i))

visited = [0 for i in range(n + 1)]
color = ['1' for i in range(m)]
flag = 1


def dfs(curr):
    nonlocal flag
    visited[curr] = 1
    for i in adj[curr]:
        if visited[i[0]] == 0:
            dfs(i[0])
        elif visited[i[0]] == 1:
            color[i[1]] = '2'
            flag = 2
    visited[curr] = 2


for n in range(1, n + 1):
    if visited[n] == 0:
        dfs(n)

if flag == 1:
    stdout.write("1\n")
    stdout.write(' '.join(color) + "\n")
else:
    stdout.write("2\n")
    stdout.write(' '.join(color) + "\n")
