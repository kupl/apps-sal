n = int(input())
a = input()
b = input()

arr = list()
arr.append('abc' * n)
arr.append('acb' * n)
arr.append('a' * n + 'b' * n + 'c' * n)
arr.append('a' * n + 'c' * n + 'b' * n)
arr.append('b' * n + 'a' * n + 'c' * n)
arr.append('b' * n + 'c' * n + 'a' * n)
arr.append('c' * n + 'a' * n + 'b' * n)
arr.append('c' * n + 'b' * n + 'a' * n)

flag = False
for s in arr:
    if s.find(a) == -1 and s.find(b) == -1:
        print("YES")
        print(s)
        flag = True
        break
if not flag:
    print("NO")
