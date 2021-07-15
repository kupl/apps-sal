x = int(input())
li = []
for i in range(1,100):
    for j in range(2,12):
        if i ** j <= x:
            if i**j not in li:
                li.append(i**j)
print(max(li))
