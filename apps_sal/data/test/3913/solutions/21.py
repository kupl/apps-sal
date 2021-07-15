n = int(input())
s = input()
already = set()
for i in s:
    if i != '*':
        already.add(i)
ans = [chr(ord('a') + i) for i in range(26)]
ans = set(ans)
for i in range(int(input())):
    cur = input()
    can = True
    clos = set() #should be closed
    for j in range(n):
        if s[j] == '*':
            clos.add(cur[j])
        elif s[j] != cur[j]:
            can = False
            break
    if can:
        if (already & clos) != set():
            can = False
    if can:
        ans = (ans & clos)
print(len(ans))

