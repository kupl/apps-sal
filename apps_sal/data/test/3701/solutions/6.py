n, a, b = map(int, input().split())
s = input()
k = sum(map(lambda x,y: x=='1' and y=='0', s, s[1:]))
k += s[0] == '0'
print (b+min(a,b)*(k-1) if k else 0)
