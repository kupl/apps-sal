n = int(input())
list = []
ans = 0
ptr = 1
for i in range(2 * n):
    s = input()
    if s[0] == 'a':
        list.append(int(s[4:]))
    elif len(list) == 0:
        ptr += 1
    elif list[-1] == ptr:
        list.pop()
        ptr += 1
    else:
        list = []
        ans += 1
        ptr += 1
print(ans)
