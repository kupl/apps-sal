n = int(input())
dict = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(n):
    s = input()
    if s[0] in dict:
        dict[s[0]] += 1
data = ['M', 'A', 'R', 'C', 'H']
ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += dict[data[i]] * dict[data[j]] * dict[data[k]]
print(ans)
