s = [input() for i in range(3)]
turn = ["a", "b", "c"]
t = 0
for i in range(300):
    if len(s[t]) == 0:
        print((turn[t].upper()))
        break
    if turn[t] == s[t][0]:
        s[t] = s[t][1:]
    else:
        tt = turn.index(s[t][0])
        s[t] = s[t][1:]
        t = tt
