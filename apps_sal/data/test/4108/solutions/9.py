from collections import Counter
s = [i for i in str(input())]
t = [h for h in str(input())]
s1 = Counter(s).most_common()
t1 = Counter(t).most_common()
if len(s1) != len(t1):
    print('No')
else:
    z = 'Yes'
    for j in range(len(s1)):
        if s1[j][1] != t1[j][1]:
            z = 'No'
            break
    print(z)
