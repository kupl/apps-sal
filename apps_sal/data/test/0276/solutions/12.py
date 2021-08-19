n = int(input())
a = []
b = ['red', 'purple', 'yellow', 'orange', 'blue', 'green']
x = {'purple': 'Power', 'blue': 'Space', 'orange': 'Soul', 'yellow': 'Mind', 'green': 'Time', 'red': 'Reality'}
for i in range(n):
    a.append(input())
ans = []
for i in b:
    if i not in a:
        ans.append(x[i])
print(len(ans))
for i in ans:
    print(i)
