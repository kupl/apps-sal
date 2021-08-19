str = input()
m = 0
for i in ['a', 'b', 'c']:
    if str.find(i) != -1:
        for j in ['a', 'b', 'c']:
            if i != j and str.find(j) != -1:
                m = max(m, str.rindex(j) - str.find(i))
print(m)
