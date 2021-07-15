n = int(input())
t = list(map(int, input().split()))

p = [bin(i) for i in t]
p = ['0' * (32 - len(i)) + i[2: ] for i in p]
p = [''.join(i) for i in zip(*p)]

x = 0
for i in range(30):
    x = p[i]
    if '1' in x and not any(all(x[k] == y[k] for k in range(n) if x[k] == '1') for y in p[i + 1: ]): break        

t = [str(t[k]) for k in range(n) if x[k] == '1']
print(len(t))
print(' '.join(t))
