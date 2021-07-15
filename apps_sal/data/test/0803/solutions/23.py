n=int(input())
s=input()
if s.count('x')>=s.count('X'):
    print(n//2-s.count('X'))
    s=s.replace('x','X',n//2-s.count('X'))
    print(s)
else:
    print(n//2-s.count('x'))
    s=s.replace('X','x',n//2-s.count('x'))
    print(s)
