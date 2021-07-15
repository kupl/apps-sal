h, w = map(int, input().split())
go = [[[] for x in range(w)] for y in range(h)]
s = input()
t = input()
c1 = s[0] == '<' and s[h - 1] == '>' and t[0] == 'v' and t[w - 1] == '^'
c2 = s[0] == '>' and s[h - 1] == '<' and t[0] == '^' and t[w - 1] == 'v'
print("YES" if c1 or c2 else "NO")
