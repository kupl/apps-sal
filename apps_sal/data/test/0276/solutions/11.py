d = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
n = int(input())
temp = set()
for i in range(n):
    temp |= {d[input()]}
ans = set()
for i in d:
    ans |= {d[i]}
ans = ans - temp
print(len(ans))
for i in ans:
    print(i)
