s=[input() for i in range(3)]
turn=["a","b","c"]
t=0
while s[t]:
    tt=turn.index(s[t][0])
    s[t]=s[t][1:]
    t=tt
print(turn[t].upper())
