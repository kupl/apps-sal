acgt = ['A', 'C', 'G', 'T']
S = input()
count = 0
max = 0
for i in S:
    if i in acgt:
        count += 1
    elif count > max:
        max = count
        count = 0
if count > max:
    max = count
    count = 0
print(max)
