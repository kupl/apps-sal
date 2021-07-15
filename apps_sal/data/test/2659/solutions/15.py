k = int(input())

def func(a):
    s = 0
    for i in str(a):
        s += int(i)
    return a/s

candidate_lst = []
for i in range(18):
    for j in range(1, 150):
         candidate_lst.append(int(str(j) + '9' * i))
candidate_lst = sorted(list(set(candidate_lst)))

count = 0
index = -1
snuke = 1
while count < k:
    min_snuke = 10**100
    for m, i in enumerate(candidate_lst[index+1:]):
        if i > 100*snuke:
            break
        po_snuke = func(i)
        if min_snuke > po_snuke:
            min_snuke = po_snuke
            next_snuke = i
            next_index = m
    print(next_snuke)
    snuke = next_snuke
    index = index + next_index + 1
    count += 1          
