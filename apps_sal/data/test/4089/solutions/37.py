N = int(input())
lst = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while N > 0:
    ans = lst[(N - 1) % 26] + ans
    N = (N - 1) // 26
print(ans)
