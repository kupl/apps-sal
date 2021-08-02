n = int(input())
a = list(map(int, input().split()))
s = [0] * 3
for i in range(3):
    s[i] = sum(a[i:n:3])

if max(s) == s[0]:
    print('chest')
elif max(s) == s[1]:
    print('biceps')
else:
    print('back')
