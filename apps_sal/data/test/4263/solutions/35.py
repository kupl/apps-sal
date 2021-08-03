S = input()

lst = ['A', 'C', 'G', 'T']
count = 0
top = 0

for i in S:
    if i in lst:
        count += 1
    else:
        if count > top:
            top = count
        count = 0
if count > top:
    top = count
print(top)
