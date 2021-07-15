elem = int(input())
string = input()
ar = []
for x in range(len(string)):
    ar.append(string[x])

first = 'a'
second = 'a'
count = 0
new_ar = []
for x in range(len(ar)):
    if x%2==0:
        first = ar[x]
        second = ar[x+1]
        if first != second:
            new_ar.append(first)
            new_ar.append(second)
        else:
            count=count+1
            new_ar.append('a')
            new_ar.append('b')
print(count)
print(''.join(str(i) for i in new_ar))
