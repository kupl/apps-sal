arr = "M S L XL XS XXL XXS XXXL XXXS"
arr.split(" ")
n = int(input())
a = []
b = []
for i in range(n):
    s = input()
    a.append(s)

for i in range(n):
    s = input()
    b.append(s)
lol = []
for i in b:
    if(i in a):
        a[a.index(i)] = '1'
    else:
        lol.append(i)
print(len(lol))
