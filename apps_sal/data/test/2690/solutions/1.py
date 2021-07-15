s = input()
p1 = [i for i in range(len(s)) if s[i] == 'a']
p2 = [i for i in range(len(s)) if s[i] == 'b']
p3 = [i for i in range(len(s)) if s[i] == 'c']
xs = [abs(i-j) for i in p1 for j in p2]
ys = [abs(i-j) for i in p1 for j in p3]
zs = [abs(i-j) for i in p3 for j in p2]
rs = xs + ys + zs
print(max(rs))
