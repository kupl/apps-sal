n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = set(map(int, input().split()))
ans = []
for but in x:
    if but in y:
        ans.append(but)
print(' '.join(map(str, ans)))

