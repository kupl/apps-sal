s=[list(input()) for i in range(3)]
turn=["a","b","c"]
t=0
while s[t]:
    t=turn.index(s[t].pop(0))
print(turn[t].upper())
