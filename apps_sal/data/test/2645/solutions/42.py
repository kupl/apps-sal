s = input()
N = len(s)
D = {'g': 0, 'p': 0}
for i in range(N):
    D[s[i]] += 1
my_p = N // 2
score = my_p - D['p']
print(score)
