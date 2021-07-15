n = int(input())

plus,minus = [],[]
for i in range(n):
    a,b = map(int,input().split())
    plus.append(a+b)
    minus.append(a-b)

plus.sort()
minus.sort()

print(max(plus[-1]-plus[0],minus[-1]-minus[0]))
