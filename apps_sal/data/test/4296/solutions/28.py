s = sum(list(map(int, input().split())))
ans = 'bust' if s > 21 else 'win'
print(ans)
