n = int(input())
s = input()
cnt = 0
abc = 'ABC'
for i in range(n - 2):
    for j in range(3):
        if s[i + j] != abc[j]:
            break
        if j == 2:
            cnt = cnt + 1
print(cnt)
