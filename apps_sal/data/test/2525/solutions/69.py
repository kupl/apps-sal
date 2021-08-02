s = input()
q = int(input())
flag = 1
f = ''
b = ''
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == '1':
        flag *= -1
    else:
        if flag == 1:
            if query[1] == '1':
                f += query[2]
            else:
                b += query[2]
        else:
            if query[1] == '1':
                b += query[2]
            else:
                f += query[2]
ans = f[::-1] + s + b
if flag == -1:
    ans = ans[::-1]
print(ans)
