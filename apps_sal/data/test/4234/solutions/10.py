n = int(input())
st = input()
ind = 0
kol = 0
new = ""
i = 0
while i < n:
    new += st[i]
    j = i + 1
    while j < n and st[j] == st[i] and ind % 2 == 0:
        j += 1
        kol += 1
    i = j
    ind += 1
if len(new) % 2 == 1:
    new = new[:-1]
    kol += 1
print(kol)
print(new)
