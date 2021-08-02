n = int(input())
string = input()
ans = string[0]
count = 0
index = []
for q in range(1, n):
    if len(ans) % 2 == 1:
        if ans[-1] != string[q]:
            ans += string[q]
        else:
            count += 1
    else:
        ans += string[q]

if len(ans) % 2 != 0:
    print(count + 1)
    print(ans[:-1])
else:
    print(count)
    print(ans)
