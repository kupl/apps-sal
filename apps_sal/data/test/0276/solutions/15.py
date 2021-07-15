n = int(input())
l = ['Power','Time','Space','Soul','Reality','Mind']
a = ['purple','green','blue','orange','red','yellow']
x = []
for i in range(n):
    s = input()
    x.append(s)
print(6-len(x))
for i in a:
    if(i not in x):
        print(l[a.index(i)])
