n = str(input())
st = "heidi"
cnt = 0
for i in n:
    if i == st[cnt]:
        cnt += 1
    if(cnt == 5):
        break
print('YES' if cnt == 5 else 'NO')
