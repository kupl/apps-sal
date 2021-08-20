N = int(input())
s = input()
que = []
for i in range(N):
    que.append(s[i])
    if len(que) >= 3 and que[-3:] == ['f', 'o', 'x']:
        que.pop()
        que.pop()
        que.pop()
print(len(que))
