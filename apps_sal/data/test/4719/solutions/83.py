n = int(input())
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dict = {}
for i in range(n):
    a = input()
    for j in data:
        if j not in dict:
            dict[j] = a.count(j)
        else:
            dict[j] = min(dict[j], a.count(j))
ans = []
for i in dict:
    ans.append(i * dict[i])
print(*ans, sep='')
