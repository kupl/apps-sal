x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ans = set(())

ans.add((x3 + x1 - x2, y3 + y1 - y2))
ans.add((x3 + x2 - x1, y3 + y2 - y1))

ans.add((x2 + x3 - x1, y2 + y3 - y1))
ans.add((x2 + x1 - x3, y2 + y1 - y3))

ans.add((x1 + x3 - x2, y1 + y3 - y2))
ans.add((x1 + x2 - x3, y1 + y2 - y3))
# print(ans)
print(len(ans))
for i in ans:
    print(' '.join(str(j) for j in i), end='\n')
