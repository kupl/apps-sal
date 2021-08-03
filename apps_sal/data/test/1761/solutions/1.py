n = int(input())
s1 = ['<3']
for i in range(n):
    s = input()
    s1.append(s)
    s1.append('<3')
s = input()
j = 0
k = 0
for i in s:
    if i == s1[j][k]:
        if len(s1[j]) == k + 1:
            j += 1
            if j == len(s1):
                print('yes')
                return
            k = 0
        else:
            k += 1
if len(s1) == j and len(s1[j]) == k:
    print('yes')
else:
    print('no')
