t = int(input())
while t:
    t -= 1
    s = input()
    s = s.rstrip('0')
    s = s[-1::-1]
    s = s.rstrip('0')
    s = s[-1::-1]
    c = 0
    l = len(s)
    print(s.count('0'))
