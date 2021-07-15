input()
num = list(map(int, input().split()))
ans = []
for i in num:
    ans.append(i if i & 1 else i-1)
print(' '.join(str(i) for i in ans))

