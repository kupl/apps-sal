n = int(input())
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list = [[] for _ in range(26)]
ans = []

for i in range(n):
    s = input()
    for j in range(26):
        list[j].append(s.count(alp[j]))

for i in range(26):
    for j in range(min(list[i])):
        ans.append(alp[i])

ans = sorted(ans)

for i in ans:
    print(i, end = '')
