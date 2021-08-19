def find(list, v):
    if list[v] != v:
        list[v] = find(list, list[v])
    return list[v]


def union(list, a, b):
    list[a] = b


d = [i for i in range(26)]
ans = []
n = int(input())
s1 = input()
s2 = input()
for i in range(n):
    a = find(d, ord(s1[i]) - ord('a'))
    b = find(d, ord(s2[i]) - ord('a'))
    if a == b:
        continue
    union(d, a, b)
    ans.append((chr(ord('a') + a), chr(ord('a') + b)))
print(len(ans))
for (a, b) in ans:
    print(a, b)
