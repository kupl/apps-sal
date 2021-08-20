N = int(input())
S = input()
ans = 0
max = 0
for s in S:
    if s == 'I':
        ans += 1
    else:
        ans -= 1
    if max < ans:
        max = ans
print(max)
