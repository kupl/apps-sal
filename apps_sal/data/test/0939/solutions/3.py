# FlagDay

data = input().split(" ")
dances = int(data[1])
totalDancers = int(data[0])

dict = {}
for d in range(dances):
    dancers = input().split(" ")
    dancers = [int(x) for x in dancers]
    i = 0
    while i < 3:
        dict.setdefault(dancers[i], i)
        if dancers[i] in dict:
            if dict[dancers[i]] != i:
                dancers[dict[dancers[i]]], dancers[i] = dancers[i], dancers[dict[dancers[i]]]
                dict[dancers[i]] = i
        else:
            dict.setdefault(dancers[i], i)
        i += 1
ans = ""
for i in range(1, totalDancers):
    ans = ans + str(dict[i] + 1) + " "
ans = ans + str(dict[totalDancers] + 1)
print(ans)
