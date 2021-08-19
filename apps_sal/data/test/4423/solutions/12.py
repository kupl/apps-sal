n = int(input())
s = []
for i in range(n):
    s.append((input() + ' ' + str(i)).split())
for i in range(n):
    s[i][1] = int(s[i][1])
s.sort(key=lambda x: x[1], reverse=True)
s.sort(key=lambda x: x[0])
for i in s:
    print(int(i[2]) + 1)
