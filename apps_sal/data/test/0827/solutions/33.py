

N = int(input())
T = input()


l = 10**10
s = '110' * ((10**5) + 1)
ans = 0
if T == '1':
    ans = l * 2
else:
    for i in range(3):
        if s[i:N + i] == T:
            ans = l - ((i + N - 1) // 3)
            break
print(ans)
