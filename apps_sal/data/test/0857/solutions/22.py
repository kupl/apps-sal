n, m = map(int, input().split())
x = [int(q) for q in input().split()]
y = [int(q) for q in input().split()]
ans = []
for i in range(len(x)):
    if x[i] in y:
        ans.append(x[i])
for item in ans:
    print(item, end=" ")
