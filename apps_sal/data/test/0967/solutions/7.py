input()
t=[int(x) for x in input().split()]
m=[True]+[t[i]>t[i+1] for i in range(len(t)-1)]
print(len(m)-1-list(reversed(m)).index(True))
