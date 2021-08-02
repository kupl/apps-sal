# cook your dish here
lst = []
for _ in range(int(input())):
    lst.append(input())
m = int(input())
k = input()
lst1 = []
for i in range(len(k)):
    for j in range(i + 1, len(k) + 1):
        lst1.append(k[i:j])
count = 0
lst1 = set(lst1)
for i in lst1:
    for j in lst:
        if i == j:
            # print(i,j)
            count += 1
            break
print(count)
