names = [chr(ord('A') + i) for i in range(26)]
names += ['A' + chr(ord('a') + i) for i in range(26)]

n, k = list(map(int, input().split()))
a = input().split()

for i, a_i in enumerate(a):
    if a_i == 'NO':
        names[i+k-1] = names[i]

print(' '.join(names[:n]))



